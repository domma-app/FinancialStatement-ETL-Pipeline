from utils.monitor.monitor_system import monitor_resources  
from pdf2image import convert_from_path

import PyPDF2
import pytesseract
import os


def extract_text_from_pdf(pdf_path):
    """Get text from PDF file using both normal extraction and OCR if needed"""
    text = ""
    
    # Try normal PDF text extraction 
    try:
        # monitor_resources("Extracting text from PDF")  
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"  # Add newline for clarity
        # monitor_resources("Finished text extraction from PDF") 
    except Exception as e:
        print(f"Error reading PDF file: {pdf_path} - {str(e)}")
        return None
        
    # If no text found, try OCR
    if text.strip() == "":
        print("No text found in PDF, trying OCR...")
        try:
            # monitor_resources("Converting PDF to images")  
            # Convert PDF to images
            images = convert_from_path(pdf_path)
            # monitor_resources("Finished converting PDF to images")  
            
            # Do OCR on each image
            text = ""
            for i, image in enumerate(images):
                # monitor_resources(f"Running OCR on page {i+1}")  
                page_text = pytesseract.image_to_string(image)
                text += f"\n=== Page {i+1} ===\n"
                text += page_text + "\n" # Add page separator for clarity
                # monitor_resources(f"Finished OCR on page {i+1}")  
                
        except Exception as e:
            print(f"Error doing OCR on PDF: {pdf_path} - {str(e)}")
            return None
            
    return text

def extract_pdfs_from_folder(input_folder="input"):
    """Extract text from all PDFs in the input folder"""
    extracted_texts = {}
    
    # Create input folder if it doesn't exist
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"Created {input_folder} directory")
        return extracted_texts
    
    # Process each PDF in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            print(f"Processing: {pdf_path}")
            
            # Extract text from PDF
            text = extract_text_from_pdf(pdf_path)
            if text:
                extracted_texts[filename] = text
                
    return extracted_texts
