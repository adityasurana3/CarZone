from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def photo(self,object):
        return format_html("<img src='{}' width='40' style='border-radius:50px;' />".format(object.thumbnail.url))
    photo.short_discription = "Photo"
    list_display=['id','photo','first_name','last_name','designation','created_date']
    list_display_links=['id','photo','first_name']
    search_fields=['first_name','last_name','designation']
    list_filter=('designation',)
