from django.contrib import admin

# Register your models here.
from .models import Project

class ProjectModelAdmin(admin.ModelAdmin):
	list_display = ["name" , "description" , "updated", "timestamp"]
	list_display_links = ["name"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["name"]

	class Meta:
		model = Project


admin.site.register(Project, ProjectModelAdmin)