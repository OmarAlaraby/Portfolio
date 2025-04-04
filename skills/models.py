from django.db import models

# Create your models here.

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('track1', 'Track 1'),
        ('track2', 'Track 2'),
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)  # FontAwesome icon class
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='track1')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['category', 'order']
