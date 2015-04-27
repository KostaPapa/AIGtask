"""
<Program Name>
  admin.py

<Author>
  Kostaq Papa <kp967@nyu.edu>

<Started>
  April 26, 2015 

<Copyright>
  See LICENSE for licensing information.

<Purpose>
  ModelAdmin class is the representation of a model in the admin interface. 
  Usually, these are stored in a file named admin.py in the application. 
  See 'https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#modeladmin-objects'
  for more information.
"""

from django.contrib import admin
from .models import Join

class CustomJoinAdmin(admin.ModelAdmin):
  """
  <Purpose>
    User joins the web app via the admin interface.
      
  <Arguments>
    admin.ModelAdmin:
      Each model is a Python class that subclasses django.contrib.ModelAdmin.

  <Exceptions>
    None.

  <Side Effects>
    None.

  <Returns>
    None.
  """

  list_display = ['email', 'timestamp', 'updated']
  
  class Meta:
    model = Join





admin.site.register(Join, CustomJoinAdmin)
