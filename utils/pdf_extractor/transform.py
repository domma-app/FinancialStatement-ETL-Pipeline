def clean_text(text):
    """Clean and normalize extracted text"""
    if not text:
        return text
        
    # Split into lines and remove empty lines
    lines = [line.strip() for line in text.split('\n')]
    lines = [line for line in lines if line]
    
    # Remove multiple spaces
    lines = [' '.join(line.split()) for line in lines]
    
    return '\n'.join(lines)

def transform_extracted_texts(extracted_texts):
    """Transform all extracted texts"""
    transformed_texts = {}
    
    for filename, text in extracted_texts.items():
        # Clean the text
        cleaned_text = clean_text(text)
        if cleaned_text:
            transformed_texts[filename] = cleaned_text
            
    return transformed_texts

