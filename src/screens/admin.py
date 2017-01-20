from django.contrib import admin

# Register your models here.
from .models import Screen

class ScreenModelAdmin(admin.ModelAdmin):
	list_display = ["name" , "orientation" ,  "project" , "updated", "timestamp"]
	list_display_links = ["name"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["name"]

	class Meta:
		model = Screen


admin.site.register(Screen, ScreenModelAdmin)