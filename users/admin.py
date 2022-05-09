from email.headerregistry import Group
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import*

class profileadmin(admin.ModelAdmin):
    list_display = ('user','image')


admin.site.register(Profile,profileadmin)
admin.site.site_header='Administración del refugio'

