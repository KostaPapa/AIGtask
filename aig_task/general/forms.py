"""
<Program Name>
  forms.py

<Author>
  Kostaq Papa <kp967@nyu.edu>

<Started>
  April 26, 2015 

<Copyright>
  See LICENSE for licensing information.

<Purpose>
  It's where the django documentation recommends placing all forms code. 
  Keeps code easily maintainable.
"""

from django import forms
from .models import Join

class EmailForm(forms.Form):
  """
  <Purpose>
    Allows a user to join by typing their email address in the form.
      
  <Arguments>
    forms.Form:
      Each form is a Python class that subclasses django.forms.Form.

  <Exceptions>
    None.

  <Side Effects>
    None.

  <Returns>
    None.
  """
  
  username = forms.CharField(required=False)
  email = forms.EmailField()


class JoinForm(forms.ModelForm):
  class Meta:
    model = Join
    fields = ["email",]