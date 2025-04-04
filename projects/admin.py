from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description', 'technologies')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'technologies', 'order')
        }),
        ('URLs', {
            'fields': ('github_url', 'live_url', 'api_docs_url'),
            'classes': ('collapse',),
            'description': 'Project links for GitHub, live site, and API documentation'
        }),
    )
