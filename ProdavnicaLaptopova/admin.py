from django.contrib import admin
from .models import Segment, Laptop

@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'slug']
    prepopulated_fields = {'slug': ('naziv',)}

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'slug', 'cena', 'raspoloziv', 'kreiran', 'azuriran']

    list_filter = ['raspoloziv', 'kreiran', 'azuriran']

    list_editable = ['cena', 'raspoloziv']
    prepopulated_fields = {'slug': ('naziv',)}

