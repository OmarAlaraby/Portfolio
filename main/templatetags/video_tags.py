import re
from django import template

register = template.Library()

@register.filter
def youtube_id(url):
    """
    Extract the YouTube video ID from a URL.
    Handles multiple YouTube URL formats.
    """
    if not url:
        return ''
        
    pattern = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    return ''

@register.filter
def vimeo_id(url):
    """
    Extract the Vimeo video ID from a URL.
    """
    if not url:
        return ''
        
    pattern = r'vimeo\.com\/(?:.*\/)?([0-9]+)'
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    return '' 