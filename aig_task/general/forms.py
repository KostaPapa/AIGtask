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


class JoinForm(forms.ModelForm):
  class Meta:
    model = Join
    fields = ["email", "text",]