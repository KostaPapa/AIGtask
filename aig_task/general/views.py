"""
<Program Name>
  views.py

<Author>
  Kostaq Papa <kp967@nyu.edu>

<Started>
  April 26, 2015 

<Copyright>
  See LICENSE for licensing information.

<Purpose>
  A view is a Python function that takes a Web request and returns
  a Web response. This response can be the HTML contents of a Web page, 
  or a redirect, or a 404 error, or an XML document, or an image, etc. 
  The view itself contains whatever arbitrary logic is necessary to return 
  that response.
"""

from django.shortcuts import render, HttpResponseRedirect
from .forms import JoinForm
from .models import Join
import uuid

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""

	return ip

def get_ref_id():
	ref_id = str(uuid.uuid4()).replace('-', '').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id


def words(request, ref_id):
	

	context = {"ref_id": ref_id}
	template = "words.html"
	return render(request, template, context)

def home(request):
	word_counter = 1
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		email = (form.cleaned_data['email'])
		text = (form.cleaned_data['text'])
		new_join_old, created = Join.objects.get_or_create(email=email, text=text)
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()

			for word in new_join_old.text:
				if (word == ' '):
					word_counter = word_counter + 1
			print (word_counter)



		return HttpResponseRedirect	("/%s" %(new_join_old.ref_id))
		
	context = {"form": form}
	template = "home.html"

	return render(request, template, context)
