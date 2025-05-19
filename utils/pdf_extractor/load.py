import os

def save_text_to_file(text, filename, output_folder="output"):
    """Save processed text to file"""
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Create output path
    output_path = os.path.join(output_folder, f"{filename}.txt")
    
    # Save the text
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return output_path
    except Exception as e:
        print(f"Error saving file {output_path}: {str(e)}")
        return None

def load_texts(transformed_texts, output_folder="output"):
    """Save all transformed texts to files"""
    saved_files = []
    
    for filename, text in transformed_texts.items():
        # Remove .pdf extension if present
        base_name = filename.replace('.pdf', '')
        
        # Save the text
        output_path = save_text_to_file(text, base_name, output_folder)
        if output_path:
            saved_files.append(output_path)
            print(f"Saved: {output_path}")
            
    return saved_files

if __name__ == "__main__":
    # Test with sample text
    sample_texts = {
        "test1.pdf": "This is a test document",
        "test2.pdf": "This is another test"
    }
    
    saved = load_texts(sample_texts)
    print(f"\nSaved {len(saved)} files") 