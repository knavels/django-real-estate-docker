from django.contrib import admin
from . import models

class ContactAdmin(admin.ModelAdmin):
    """Handles the admin area for contacts"""
    list_display = ('id', 'name', 'listing', 'phone', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(models.Contact, ContactAdmin)
