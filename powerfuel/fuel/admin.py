from django.utils.html import format_html
from django.contrib import admin
from .models import Fuel
from .forms import FuelForm

@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    form = FuelForm
    list_display = ['name', 'price', 'description', 'photo_display']

    def photo_display(self, obj):
        if obj.photo_url:
            return format_html('<img src="{}" style="max-width:200px;max-height:200px;" />', obj.photo_url)
        else:
            return "No Photo"

    photo_display.allow_tags = True
    photo_display.short_description = 'Photo Preview'
