from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Media(models.Model):
	name = models.CharField(max_length=120)
	content  = models.TextField()
	image = models.FileField(null = True , blank = True)
	updated = models.DateTimeField(auto_now = True , auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False , auto_now_add = True)


	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name