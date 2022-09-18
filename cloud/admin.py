from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'location', 'file_type', 'size', 'upload_datetime']
	list_filter = ['upload_datetime','file_type']

	class Meta:
		model = File

admin.site.register(File, FileAdmin)
