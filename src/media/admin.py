from django.contrib import admin

# Register your models here.
from .models import Media

class MediaModelAdmin(admin.ModelAdmin):
	list_display = ["name" , "updated", "timestamp"]
	list_display_links = ["name"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["name", "content"]

	class Meta:
		model = Media
		js = (
			"/static/js/custom.js"
		)


admin.site.register(Media, MediaModelAdmin)