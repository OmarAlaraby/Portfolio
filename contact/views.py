from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
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
            
            # Prepare email notification
            try:
                subject = f"New Contact: {contact_message.subject}"
                
                # Prepare email context
                context = {
                    'name': contact_message.name,
                    'email': contact_message.email,
                    'subject': contact_message.subject,
                    'message': contact_message.message,
                    'date': contact_message.date_sent.strftime("%B %d, %Y at %I:%M %p")
                }
                
                # Render email templates
                text_content = render_to_string('contact/email_template.txt', context)
                html_content = render_to_string('contact/email_template.html', context)
                
                # Create email message
                email = EmailMultiAlternatives(
                    subject=subject,
                    body=text_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.CONTACT_EMAIL],
                )
                
                # Attach HTML version
                email.attach_alternative(html_content, "text/html")
                
                # Send email
                email.send()
                
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                print(f"Email sending error: {e}")
                messages.error(request, 'Your message has been saved, but there was a problem sending the email notification. Please try again later.')
                
            return redirect('index')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    return redirect('index')
