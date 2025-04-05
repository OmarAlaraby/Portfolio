# Email Configuration for Portfolio Site

This document explains how to correctly set up email functionality for the contact form on your Render.com deployment.

## Understanding the Issue

If the contact form is not sending emails on your hosted website, it's likely due to missing or incorrect environment variables for email configuration.

## Setting Up Gmail for SMTP

The simplest approach is to use Gmail as your SMTP server:

1. **Create an App Password** (required if you have 2-factor authentication):
   - Go to your Google Account (https://myaccount.google.com/)
   - Select "Security"
   - Under "Signing in to Google", select "App passwords" 
     (If you don't see this option, 2-Step Verification may not be enabled)
   - Select "Mail" as the app and "Other" as the device
   - Enter a name (e.g., "Django Portfolio")
   - Click "Generate"
   - Copy the 16-character password

2. **Allow Less Secure Apps** (if not using an App Password):
   - This is only recommended for testing
   - Go to https://myaccount.google.com/lesssecureapps
   - Turn "Allow less secure apps" to ON

## Configuring Environment Variables on Render.com

1. **Log in** to your Render.com account
2. **Navigate** to your web service dashboard
3. **Click** on "Environment" in the left sidebar
4. **Add** the following environment variables:

   ```
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password-or-regular-password
   DEFAULT_FROM_EMAIL=noreply@omar-alaraby-portfolio.onrender.com
   CONTACT_EMAIL=your-email@gmail.com
   ```

5. **Click** "Save Changes"
6. **Redeploy** your application

## Testing Your Email Configuration

1. Visit your portfolio site
2. Fill out and submit the contact form
3. Check if you receive the email
4. If not, check the logs on Render.com for error messages

## Troubleshooting

If emails still don't work:

1. **Check your spam folder** - emails might be marked as spam
2. **Verify environment variables** are correctly set on Render.com
3. **Consider using a different email service** like SendGrid or Mailgun
4. **Check Render.com logs** for specific error messages

## Using SendGrid as an Alternative

If Gmail doesn't work, SendGrid offers a free tier:

1. **Create** a SendGrid account
2. **Set up** a Sender Identity
3. **Create** an API Key
4. **Configure** your environment variables:

   ```
   EMAIL_HOST=smtp.sendgrid.net
   EMAIL_PORT=587
   EMAIL_HOST_USER=apikey
   EMAIL_HOST_PASSWORD=your-sendgrid-api-key
   DEFAULT_FROM_EMAIL=noreply@omar-alaraby-portfolio.onrender.com
   CONTACT_EMAIL=your-email@gmail.com
   ```

5. **Redeploy** your application 