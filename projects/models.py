from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
import os

# Create your models here.

class Project(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='image', 
                                help_text="Choose the type of media for this project")
    image = CloudinaryField(
        'image', 
        folder='portfolio/projects',
        transformation={
            'quality': 'auto:good', 
            'fetch_format': 'auto',
            'width': 'auto',
            'crop': 'limit',
            'max_width': 1000
        },
        overwrite=True,
        resource_type='auto',
        use_filename=True,
        unique_filename=True,
        blank=True,
        null=True,
        help_text="Upload an image for this project"
    )
    video = CloudinaryField(
        'video',
        folder='portfolio/videos',
        resource_type='video',
        use_filename=True,
        unique_filename=True,
        blank=True,
        null=True,
        help_text="Upload a video file directly (MP4, WebM, etc.)"
    )
    technologies = models.CharField(max_length=255)
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    api_docs_url = models.URLField(blank=True, null=True, verbose_name="API Documentation URL")
    order = models.IntegerField(default=0)
    
    def clean(self):
        if self.media_type == 'image' and not self.image:
            raise ValidationError({
                'image': 'An image is required when Media Type is set to Image.'
            })
        elif self.media_type == 'video' and not self.video:
            raise ValidationError({
                'video': 'A video file is required when Media Type is set to Video.'
            })
        
        if self.image and hasattr(self.image, 'size') and self.image.size > 5 * 1024 * 1024:  # 5MB
            raise ValidationError({
                'image': 'Image file too large (maximum size is 5MB). Please optimize or resize the image before uploading.'
            })
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
