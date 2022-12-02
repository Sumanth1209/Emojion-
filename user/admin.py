from django.contrib import admin
from .models import emo

class CompAdmin(admin.ModelAdmin):
    list_display=["uname","date","time","emotion","EU","source"]


# Register your models here.
admin.site.register(emo,CompAdmin)