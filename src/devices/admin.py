from django.contrib import admin

# Register your models here.
from .models import Device

class DeviceModelAdmin(admin.ModelAdmin):
	list_display = ["reference_no" , "status","updated", "timestamp"]
	list_display_links = ["reference_no"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["reference_no"]

	class Meta:
		model = Device


admin.site.register(Device, DeviceModelAdmin)