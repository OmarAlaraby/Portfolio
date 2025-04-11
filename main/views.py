from django.shortcuts import render
from django.contrib import messages
from projects.views import get_projects
from skills.views import get_skills
from contact.views import get_contact_info
from contact.forms import ContactForm
from .models import Profile
# Create your views here.

def get_profile():
    return Profile.objects.first()

def index(request):
    """
    Main view for the portfolio homepage that fetches and integrates data from all apps.
    
    This view aggregates data from the projects, skills, and contact apps to render
    a comprehensive portfolio page with dynamic content.
    """
    # Get data from all apps
    projects = get_projects()
    skills_data = get_skills()
    contact_info = get_contact_info()
    contact_form = ContactForm()
    profile = get_profile()
    # Get any messages from Django's message framework
    messages_from_request = messages.get_messages(request)
    
    context = {
        'projects': projects,
        'track1_skills': skills_data['track1_skills'],
        'track2_skills': skills_data['track2_skills'],
        'contact_info': contact_info,
        'form': contact_form,
        'messages': messages_from_request,
        'profile': profile,
    }
    
    return render(request, 'main/index.html', context)
