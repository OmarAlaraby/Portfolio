from django.shortcuts import render
from .models import Skill

def get_skills():
    """get all skills"""
    track1_skills = Skill.objects.filter(category='track1')
    track2_skills = Skill.objects.filter(category='track2')
    
    return {
        'track1_skills': track1_skills,
        'track2_skills': track2_skills
    }
