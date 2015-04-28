"""
<Program Name>
  models.py

<Author>
  Kostaq Papa <kp967@nyu.edu>

<Started>
  April 26, 2015 

<Copyright>
  See LICENSE for licensing information.

<Purpose>
  Provide models as a single, definitive source of information about data. 
  It contains the essential fields and behaviors of the data being stored. 
  Generally, each model maps to a single database table.
  See 'https://docs.djangoproject.com/en/1.8/topics/db/models/' for 
  more information.
"""

from django.db import models

class Join(models.Model):
  """
  <Purpose>
    Allows a user to join the web app.
      
  <Arguments>
    models.Model:
      Each model is a Python class that subclasses django.db.models.Model.

  <Exceptions>
    None.

  <Side Effects>
    None.

  <Returns>
    None.
  """

  email = models.EmailField()
  text = models.TextField('Enter Text', blank=True)

  ref_id = models.CharField(max_length=120, default='ABC')
  ip_address = models.CharField(max_length=120, default='ABC')
  
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __str__(self):
    return (self.email)

  class Meta:
    unique_together = ("email", "ref_id",)