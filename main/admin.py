from django.contrib import admin
from django.utils.html import format_html
from .models import *

class SeasonAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class CountryAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class ClubAdmin(admin.ModelAdmin):
    list_display = ["name","president","coach","country"]
    list_filter = ['country']
    search_fields = ['name','coach','president']
    ordering = ['name']
    def image_tag(self,obj):
        if obj.image:
            return format_html('<img src="{}" width="{100px}" height="100px" style="border-radius:')
        return "No Image"
    image_tag.short_description = 'Image Preview'

admin.site.register(Season,SeasonAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Club,ClubAdmin)