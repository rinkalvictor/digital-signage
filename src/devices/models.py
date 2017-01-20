from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Device(models.Model):
	STATUS_CHOICES = (
		('Active' , 'Active' ),
		('Inactive' , 'Inactive' )
	)
	reference_no = models.CharField(max_length=120)
	status  = models.CharField(
		max_length=15,
		choices=STATUS_CHOICES,
		default = 'Inactive')
	updated = models.DateTimeField(auto_now = True , auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False , auto_now_add = True)


	def __unicode__(self):
		return self.reference_no

	def __str__(self):
		return self.reference_no