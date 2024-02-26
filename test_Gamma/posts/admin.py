from django.contrib import admin

from .models import Letter, Package


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sender_full_name',
        'recipient_full_name',
        'departure_point',
        'destination_point',
        'departure_index',
        'destination_index',
        'letter_type',
        'letter_weight',
    )
    list_display_links = ('id', 'sender_full_name', 'recipient_full_name')
    list_filter = ('sender_full_name',)
    search_fields = ('sender_full_name',)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sender_full_name',
        'recipient_full_name',
        'departure_point',
        'destination_point',
        'departure_index',
        'destination_index',
        'phone',
        'package_type',
        'payment_amount',
    )
    list_display_links = ('id', 'sender_full_name', 'recipient_full_name')
    list_filter = ('sender_full_name',)
    search_fields = ('sender_full_name',)
