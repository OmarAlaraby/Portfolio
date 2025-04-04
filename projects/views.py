from django.shortcuts import render
from .models import Project

def get_projects():
    """Helper function to get all projects for use in templates"""
    return Project.objects.all()

# Create your views here.
