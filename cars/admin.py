from django.contrib import admin
from django.utils.html import format_html
from .models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def photo(self,object):
        # return format_html("<img src='{}' width='40' style='border-radius:50px' />".format(object.car_photo.url))
        return format_html(f"<img src='{object.car_photo.url}' width='40' style='border-radius:50px' />")

    list_display=['id','photo','car_title','city','color','model','year','body_style','fuel_type','is_featured']
    list_display_links=['id','photo','car_title']
    list_editable = ('is_featured',)
    search_fields=['id','car_title','city','model','body_style','fuel_type']
    list_filter=['city','model','body_style','fuel_type']