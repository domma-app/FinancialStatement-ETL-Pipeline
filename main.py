from utils.pdf_extractor.extract import extract_pdfs_from_folder
from utils.pdf_extractor.transform import transform_extracted_texts
from utils.pdf_extractor.load import load_texts

from utils.financial_statements.extract import get_financial_data
from utils.financial_statements.transform import prepare_data_for_saving
from utils.financial_statements.load import save_data_to_csv

def main():
    # Get text from PDF files
    print("=== Extracting PDFs ===")
    pdf_texts = extract_pdfs_from_folder()
    
    # Clean up the extracted texts
    print("\n=== Transforming texts ===")
    clean_texts = transform_extracted_texts(pdf_texts)
    
    # Save the cleaned texts
    print("\n=== Saving processed texts ===")
    saved_files = load_texts(clean_texts)
    
    # Find financial information in the texts
    print("\n=== Extracting financial metrics ===")
    all_financial_data = []

    # Look through each text file we processed
    for text in clean_texts.values():
        # Get financial data from this text
        financial_data = get_financial_data(text)
        # If we found any data, add it to our list
        if financial_data:
            all_financial_data.extend(financial_data)
    
    # Prepare the financial data for saving
    print("\n=== Transforming financial data ===")
    prepared_data = prepare_data_for_saving(all_financial_data)
    
    # Save the financial data to CSV
    print("\n=== Saving financial metrics ===")
    saved_data = save_data_to_csv(prepared_data)
    
    # Print a summary of what we did
    print("\n=== Summary ===")
    print(f"PDFs processed: {len(pdf_texts)}")
    print(f"Texts transformed: {len(clean_texts)}")
    print(f"Files saved: {len(saved_files)}")
    print(f"Financial records extracted: {len(saved_data)} years")
    print("\nFinancial Metrics (in millions):")
    print(saved_data)

# Only run the program if we run this file directly
if __name__ == "__main__":
    main() 