from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import ContactInfo, ContactMessage
from .forms import ContactForm

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
            contact_message = form.save()
            
            # Send email notification
            try:
                subject = f"New Contact Form Submission: {contact_message.subject}"
                
                # Create message content
                message = f"""
                You have received a new message from your portfolio website:
                
                Name: {contact_message.name}
                Email: {contact_message.email}
                Subject: {contact_message.subject}
                
                Message:
                {contact_message.message}
                
                Date: {contact_message.date_sent}
                """
                
                # Send the email
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                # Log the error but don't show technical details to the user
                print(f"Email sending error: {e}")
                messages.success(request, 'Your message has been saved, but there was a problem sending the email notification.')
                
            return redirect('index')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    return redirect('index')
