from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
import os

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    # Support for images, GIFs, and MP4 videos
    image = CloudinaryField('image', resource_type='auto', folder='portfolio/projects')
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    
    def clean(self):
        # Only check file size, no other validation
        if self.image and hasattr(self.image, 'size') and self.image.size > 10 * 1024 * 1024:  # 10MB
            raise ValidationError({
                'image': 'File too large (maximum size is 10MB).'
            })
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order', '-created_at']
