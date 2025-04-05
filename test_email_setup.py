#!/usr/bin/env python
"""
Simple test script to check email configuration.
This will print the current email backend and attempt to send a test email.
"""
import os
import sys
import socket
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.conf import settings
from django.core.mail import send_mail

def test_email_config():
    """Print the current email configuration and backend"""
    print(f"\n==== EMAIL CONFIGURATION TEST ====")
    print(f"DEBUG mode: {settings.DEBUG}")
    print(f"Running on: {socket.gethostname()}")
    print(f"Email backend: {settings.EMAIL_BACKEND}")
    
    if hasattr(settings, 'AWS_ACCESS_KEY_ID'):
        print(f"AWS access key configured: {'Yes' if settings.AWS_ACCESS_KEY_ID else 'No'}")
    
    print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
    print(f"CONTACT_EMAIL: {settings.CONTACT_EMAIL}")
    
    # Try to send a test email
    print("\nAttempting to send a test email...")
    try:
        send_mail(
            subject="Test Email from Portfolio Site",
            message="This is a test email to verify your configuration is working.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False
        )
        print("✅ Test email sent successfully!")
        print(f"If using console backend, check console output above.")
        print(f"If using SES, check your inbox at: {settings.CONTACT_EMAIL}")
    except Exception as e:
        print(f"❌ Error sending test email: {str(e)}")
        
    print("\n==== TEST COMPLETE ====")

if __name__ == "__main__":
    test_email_config() 