from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = CloudinaryField('image', folder='portfolio/profile')

    def __str__(self):
        return self.title
