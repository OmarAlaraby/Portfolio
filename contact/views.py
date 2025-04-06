from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import ContactInfo, ContactMessage
from .forms import ContactForm
from django.utils import timezone

def get_contact_info():
    """Helper function to get contact info for use in templates"""
    try:
        return ContactInfo.objects.first()
    except ContactInfo.DoesNotExist:
        return None

def save_contact_message(request):
    """Save a contact form submission to the database and send email notification"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            contact_data = form.save()
            # Prepare email notification
            try:
                subject = f"New Contact: {contact_data.subject}"
                # Prepare email context
                context = {
                    'name': contact_data.name,
                    'email': contact_data.email,
                    'subject': contact_data.subject,
                    'message': contact_data.message,
                    'date': timezone.now().strftime("%B %d, %Y at %I:%M %p")
                }
                
                # Render both text and HTML versions
                text_content = render_to_string('contact/email_template.txt', context)
                html_content = render_to_string('contact/email_template.html', context)
                
                # Send email with both versions
                send_mail(
                    subject=subject,
                    message=text_content, 
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    html_message=html_content, 
                    fail_silently=False,
                )
                
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, 'Your message has been saved, but there was a problem sending the email notification. Please try again later.')
                
            return redirect('index')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    return redirect('index')
