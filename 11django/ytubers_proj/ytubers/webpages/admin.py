from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def myPhoto(self , object):
        return format_html('<img src="{}" width="40">'.format(object.photo.url))
    
    def name(self,object):
        return format_html('<b>{}</b>'.format(object.fname.upper()))
    list_display = ('id' , 'myPhoto', 'name' , 'lname' , 'role' , 'created_at')
    list_display_links =('role',)
    list_filter = ('role' , 'fname')
    search_fields = ('role',)

admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)
