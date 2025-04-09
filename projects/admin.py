from django.contrib import admin
from .models import Project
from django.utils.html import format_html
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import re

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'order', 'featured', 'created_at', 'display_media')
    list_filter = ('featured', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    list_editable = ('order', 'featured')
    readonly_fields = ('display_media',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'technologies', 'image', 'url', 'github_url')
        }),
        ('Display Options', {
            'fields': ('order', 'featured'),
            'classes': ('collapse',)
        }),
        ('Media Preview', {
            'fields': ('display_media',),
            'description': 'Preview of uploaded media (images, GIFs, or MP4 videos)',
            'classes': ('collapse',)
        }),
    )
    
    def display_media(self, obj):
        if obj.image:
            # Check if it's a video
            if obj.image.resource_type == 'video':
                return format_html(
                    '<video width="320" height="240" controls><source src="{}" type="video/mp4">Your browser does not support the video tag.</video>',
                    obj.image.url
                )
            # It's an image or GIF
            return format_html('<img src="{}" width="320" height="auto" />', obj.image.url)
        return "No media uploaded"
    display_media.short_description = 'Media Preview'
    
    def get_youtube_or_vimeo_id(self, url):
        """Extract video ID from YouTube or Vimeo URL"""
        youtube_pattern = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
        vimeo_pattern = r'vimeo\.com\/(?:.*\/)?([0-9]+)'
        
        youtube_match = re.search(youtube_pattern, url)
        if youtube_match:
            return youtube_match.group(1)
            
        vimeo_match = re.search(vimeo_pattern, url)
        if vimeo_match:
            return vimeo_match.group(1)
            
        # Return the full URL if we can't extract an ID
        return url
        
        super().save_model(request, obj, form, change)
