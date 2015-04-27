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

from django.shortcuts import render
from .forms import EmailForm, JoinForm
from .models import Join

def home(request):
	


	# form = EmailForm(request.POST or None)
	
	# if form.is_valid():
	# 	email = (form.cleaned_data['email'])
	# 	new_join, created = Join.objects.get_or_create(email=email)
	# 	print (new_join, created)
	# 	print (new_join.timestamp)

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		email = (form.cleaned_data['email'])
		new_join_old, created = Join.objects.get_or_create(email=email)
		# new_join.save()

	context = {"form": form}
	template = "home.html"

	return render(request, template, context)
