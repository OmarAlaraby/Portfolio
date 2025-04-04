from django.contrib import admin
from .models import ContactInfo, ContactMessage

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'location')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent')
    readonly_fields = ('date_sent',)
    search_fields = ('name', 'email', 'subject', 'message')
