from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "city", "created_at")
    search_fields = ("name", "email", "city")
    list_filter = ("created_at",)
