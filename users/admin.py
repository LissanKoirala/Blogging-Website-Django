from django.contrib import admin
from .models import Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ('user','image')
    list_filter = ('image','user')
    search_fields = ('user','email')

# Register your models here.
admin.site.register(Profile, UserAdmin)
 