from __future__ import unicode_literals

from django.db import models
from projects.models import Project
from devices.models import Device

# Create your models here.
class Screen(models.Model):
	SCREEN_ORIENTATION_CHOICES = (
		('Normal (0)' , 'Normal (0)' ),
		('Rotated clockwise (90)' , 'Rotated clockwise (90)' ),
		('Upside down (180)' , 'Upside down (180)' ),
		('Rotated counterclockwise (270)' , 'Rotated counterclockwise (270)' )
	)
	name = models.CharField(max_length=120)
	orientation = models.CharField(
		max_length=50,
		choices=SCREEN_ORIENTATION_CHOICES,
		default = 'Normal (0)')
	description  = models.TextField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	device = models.ForeignKey(Device, on_delete=models.CASCADE, null = True)
	updated = models.DateTimeField(auto_now = True , auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False , auto_now_add = True)


	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name