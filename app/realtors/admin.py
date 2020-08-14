from django.contrib import admin
from . import models


class RealtorAdmin(admin.ModelAdmin):
    """Handles all admin page customization for realtors"""
    list_display = ('id', 'name', 'email', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name')
    list_editable = ('email', 'is_mvp')
    search_fields = ('name', 'email')
    list_per_page = 25

admin.site.register(models.Realtor, RealtorAdmin)
