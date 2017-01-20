from __future__ import unicode_literals

from django.db import models
# from screen.models import Screen

# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length=120)
	description  = models.TextField()
	# screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
	updated = models.DateTimeField(auto_now = True , auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False , auto_now_add = True)


	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name