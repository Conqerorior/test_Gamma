from django.contrib import admin

from .models import Letter


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sender_full_name",
        "recipient_full_name",
    )
    list_display_links = ("id", "sender_full_name", "recipient_full_name")
    list_filter = ("sender_full_name",)
    search_fields = ("sender_full_name",)
