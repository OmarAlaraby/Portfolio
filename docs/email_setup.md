# Email Configuration for Portfolio Site

This document explains how to correctly set up Gmail for sending emails from your portfolio contact form.

## Understanding the Issue

If the contact form is not sending emails on your hosted website, it's likely due to missing or incorrect environment variables for email configuration.

## Gmail SMTP Configuration

To use Gmail as your SMTP server:

1. **Create an App Password** (required if you have 2-factor authentication):
   - Go to your Google Account (https://myaccount.google.com/)
   - Select "Security"
   - Under "Signing in to Google", select "App passwords" 
     (If you don't see this option, 2-Step Verification may need to be enabled)
   - Select "Mail" as the app and "Other" as the device
   - Enter a name (e.g., "Django Portfolio")
   - Click "Generate"
   - Copy the 16-character password

2. **Allow Less Secure Apps** (if not using an App Password):
   - This is only recommended for testing
   - Note: This option is being deprecated by Google, so App Password is recommended

## Setting Environment Variables on Render.com

Add these environment variables in your Render.com dashboard:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

That's it! Your Gmail account will be used for both sending and receiving contact form emails.

## Testing Your Email Configuration

1. Visit your portfolio site
2. Fill out and submit the contact form
3. Check if you receive the email
4. If not, check the logs on Render.com for error messages

## Troubleshooting

If emails still don't work:

1. **Check your spam folder** - emails might be marked as spam
2. **Verify environment variables** are correctly set on Render.com
3. **Confirm your App Password** is correctly generated and entered
4. **Check Render.com logs** for specific error messages
5. **Try using a different email service** like SendGrid or Mailgun if Gmail doesn't work

## Alternative: Using SendGrid

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
DEFAULT_FROM_EMAIL=your-verified-email@example.com
CONTACT_EMAIL=your-email@gmail.com
``` 