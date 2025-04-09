import cloudinary
import cloudinary.uploader
from django.conf import settings
import os
import tempfile
from PIL import Image
import fitz  # PyMuPDF

def convert_pdf_to_image(pdf_path, page_number=0):
    """
    Convert a PDF file to an image.
    
    Args:
        pdf_path: Path to the PDF file
        page_number: Page number to convert (default: 0 for first page)
        
    Returns:
        Path to the generated image file
    """
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    # Get the specified page
    page = pdf_document[page_number]
    
    # Convert page to image
    pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))  # 300 DPI
    
    # Create a temporary file for the image
    temp_image = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_image_path = temp_image.name
    temp_image.close()
    
    # Save the image
    pix.save(temp_image_path)
    
    # Close the PDF
    pdf_document.close()
    
    return temp_image_path

def upload_pdf_as_image(pdf_file, folder="resumes"):
    """
    Upload a PDF file to Cloudinary and convert it to an image.
    
    Args:
        pdf_file: The PDF file to upload
        folder: The folder in Cloudinary to store the files
        
    Returns:
        Dictionary with 'pdf_url' and 'image_url' keys
    """
    # First, save the PDF to a temporary file
    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    temp_pdf_path = temp_pdf.name
    temp_pdf.close()
    
    # Write the uploaded file to the temporary file
    with open(temp_pdf_path, 'wb') as f:
        f.write(pdf_file.read())
    
    # Upload the PDF to Cloudinary
    pdf_upload_result = cloudinary.uploader.upload(
        temp_pdf_path,
        resource_type="raw",
        folder=folder,
        format="pdf"
    )
    
    # Convert the PDF to an image
    image_path = convert_pdf_to_image(temp_pdf_path)
    
    # Upload the image to Cloudinary
    image_upload_result = cloudinary.uploader.upload(
        image_path,
        folder=folder,
        format="jpg"
    )
    
    # Clean up temporary files
    os.unlink(temp_pdf_path)
    os.unlink(image_path)
    
    return {
        'pdf_url': pdf_upload_result['secure_url'],
        'image_url': image_upload_result['secure_url']
    } 