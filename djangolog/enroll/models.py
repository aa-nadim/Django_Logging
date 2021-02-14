from django.db import models
from django import forms

# Create your models here.

class EventsForm(models.Model):

	id = models.AutoField (primary_key = True)
	time = models.TextField()
	error_type = models.TextField()
	message = models.TextField()

	def __str__(self):
		return "Click on this : "+self.error_type

