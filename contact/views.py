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
                subject = f"Contact from your portfolio website: {contact_message.subject}"
                
                # Create message content
                message = f"""
                You have received a new message from your portfolio website:
                
                Name: {contact_message.name}
                
                Message:
                {contact_message.message}
                
                Date: {contact_message.date_sent.strftime("%B %d, %Y at %I:%M %p")}
                """
                
                # Send the email
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                print(f"Email sending error: {e}")
                messages.success(request, 'Your message has been saved, but there was a problem sending the email notification.')
                
            return redirect('index')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    return redirect('index')
