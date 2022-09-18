from django.contrib import admin
from .models import UrlModel
# Register your models here.

class UrlModelAdmin(admin.ModelAdmin):
    list_display = ('short_url','url')
    search_fields = ('short_url','url')

admin.site.register(UrlModel, UrlModelAdmin)

