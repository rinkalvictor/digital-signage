from __future__ import unicode_literals

from django.db import models
from media.models import Media
from projects.models import Project

# Create your models here.

class Schedule(models.Model):
	media = models.ForeignKey(Media, on_delete=models.CASCADE)
	projects = models.ManyToManyField(Project)
	name = models.CharField(max_length=120)
	start_date = models.DateField(auto_now=False, auto_now_add=False)
	end_date = models.DateField(auto_now=False, auto_now_add=False)
	start_time = models.TimeField(auto_now=False, auto_now_add=False)
	end_time = models.TimeField(auto_now=False, auto_now_add=False)
	sun = models.BooleanField(default=False)
	mon = models.BooleanField(default=False)
	tue = models.BooleanField(default=False)
	wed = models.BooleanField(default=False)
	thu = models.BooleanField(default=False)
	fri = models.BooleanField(default=False)
	sat = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now = True , auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False , auto_now_add = True)


	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name