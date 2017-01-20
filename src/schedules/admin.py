from django.contrib import admin

# Register your models here.
from .models import Schedule

class ScheduleModelAdmin(admin.ModelAdmin):
	list_display = ["name" , "media" ,  "start_date" , "end_date", "start_time", "end_time" , "updated", "timestamp"]
	list_display_links = ["name"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["name"]

	class Meta:
		model = Schedule


admin.site.register(Schedule, ScheduleModelAdmin)