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
    list_display = ('title', 'order', 'media_type', 'display_media')
    list_editable = ('order',)
    list_filter = ('media_type',)
    search_fields = ('title', 'description', 'technologies')
    readonly_fields = ('display_media',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'technologies', 'order')
        }),
        ('Media', {
            'fields': ('media_type', ('image', 'video', 'display_media')),
            'description': 'Choose either an image or video upload for this project'
        }),
        ('URLs', {
            'fields': ('github_url', 'live_url', 'api_docs_url'),
            'classes': ('collapse',),
            'description': 'Project links for GitHub, live site, and API documentation'
        }),
    )
    
    def display_media(self, obj):
        if obj.media_type == 'image' and obj.image:
            return format_html('<img src="{}" width="150" height="auto" />', obj.image.url)
        elif obj.media_type == 'video' and obj.video:
            return format_html('<video width="200" height="113" controls><source src="{}" type="video/mp4">Your browser does not support the video tag.</video>', obj.video.url)
        return "No media"
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
    
    def save_model(self, request, obj, form, change):
        if form.is_valid():
            # Only process images if we're using the image media type and there's a new image
            if obj.media_type == 'image' and 'image' in form.changed_data:
                image = request.FILES.get('image')
                if image and hasattr(image, 'content_type') and image.content_type.startswith('image'):
                    # Skip optimization for GIFs to preserve animation
                    if image.content_type == 'image/gif':
                        # Just pass through GIF files without modification
                        pass
                    # Only process if it's larger than 500KB and not a GIF
                    elif image.size > 500 * 1024:  # 500KB
                        try:
                            # Open the uploaded image
                            img = Image.open(image)
                            
                            # Calculate new dimensions maintaining aspect ratio
                            max_width = 1200
                            if img.width > max_width:
                                ratio = max_width / img.width
                                new_width = max_width
                                new_height = int(img.height * ratio)
                                img = img.resize((new_width, new_height), Image.LANCZOS)
                            
                            # Convert to optimized format
                            output = io.BytesIO()
                            
                            # Save as JPEG with 85% quality
                            if img.mode != 'RGB':
                                img = img.convert('RGB')
                            img.save(output, format='JPEG', quality=85, optimize=True)
                            output.seek(0)
                            
                            # Replace the image in the form
                            obj.image = InMemoryUploadedFile(
                                output,
                                'ImageField',
                                f"{image.name.split('.')[0]}.jpg",
                                'image/jpeg',
                                sys.getsizeof(output),
                                None
                            )
                        except Exception as e:
                            # If there's an error, just use the original image
                            print(f"Error optimizing image: {e}")
                            pass
        
        super().save_model(request, obj, form, change)
