# Cloudinary Setup for Portfolio Project

This guide explains how to set up Cloudinary for handling media files (like project images) in your portfolio project. Cloudinary provides persistent storage that doesn't get wiped when your hosting provider restarts virtual machines.

## Why Cloudinary?

- **Persistent Storage**: Files remain available regardless of server restarts
- **Global CDN**: Fast loading worldwide
- **Image Transformations**: Automatic resizing and optimization
- **Generous Free Tier**: 25GB storage and 25GB monthly bandwidth

## Setup Steps

### 1. Create a Cloudinary Account

1. Go to [Cloudinary.com](https://cloudinary.com/) and sign up for a free account
2. After signing up, you'll be taken to your dashboard

### 2. Get Your Cloudinary Credentials

From your Cloudinary dashboard, note down:
- **Cloud Name**
- **API Key**
- **API Secret**

### 3. Configure Environment Variables

Add these environment variables to your local development environment and your hosting provider (Render.com):

```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

On Render.com:
1. Go to your web service dashboard
2. Click on "Environment" in the left sidebar
3. Add the environment variables
4. Save changes and redeploy

## Using Cloudinary in the Project

The project is already configured to:
- Use Cloudinary storage in production
- Use local storage in development
- Automatically upload media files to Cloudinary

### How Project Images are Handled

Project images are now stored in the `portfolio/projects` folder in your Cloudinary account. When you upload a new project image through the Django admin, it will:

1. In development: Save locally to your `media/projects/` directory
2. In production: Upload to your Cloudinary account

The project supports various image formats:
- **JPEG/PNG/WebP**: Automatically optimized for file size and quality
- **GIF**: Preserved as-is to maintain animation
- **Other formats**: Automatically handled by Cloudinary

All existing project URLs will continue to work, and the transition should be seamless from a user perspective.

## Troubleshooting

If images are not appearing:

1. Verify your Cloudinary credentials are correct
2. Check that Cloudinary can be reached from your hosting provider
3. Look for errors in your application logs
4. Try re-uploading an image through the Django admin

### Handling Large Image Uploads (Worker Timeout Issues)

If you encounter worker timeout errors when uploading images in the admin interface (`WORKER TIMEOUT` error), try these solutions:

1. **Optimize your images before uploading**:
   - Use an image optimization tool like TinyPNG or ImageOptim
   - Resize large images to under 1200px wide
   - Convert to JPEG format with 80-85% quality
   - Aim for file sizes under 500KB

2. **If you must upload large images**:
   - Increase your server's worker timeout (on Render.com: set the `PYTHON_TIMEOUT` environment variable to a higher value like 120 or 240)
   - Consider using Cloudinary's direct upload widget for very large files
   - Upload in batches rather than many images at once

3. **Try alternate upload methods**:
   - Upload directly via the Cloudinary dashboard
   - If you get timeouts in the admin, try uploading via the Cloudinary web interface and then select the image in Django admin using the existing URL

The project has been configured with automatic image optimization in the admin interface to help prevent timeouts, but very large images may still cause issues.

## Manual Image Upload

You can also manually upload images to Cloudinary:

1. Go to your Cloudinary dashboard
2. Click "Media Library"
3. Click "Upload" to add new images
4. Use the public URL in your Django admin 