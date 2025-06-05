from utils.pdf_extractor.extract import extract_pdfs_from_folder
from utils.pdf_extractor.transform import transform_extracted_texts
from utils.pdf_extractor.load import load_texts

from utils.financial_statements.extract import get_financial_data
from utils.financial_statements.transform import prepare_data_for_saving
from utils.financial_statements.load import save_data_to_csv

from utils.predict.predictor import stock_purchase_recommendation

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

import io
import os
import shutil
import uvicorn

app = FastAPI()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Upload a PDF file and get the financial metrics and stock purchase recommendation.
    """
    try:
        # Save the uploaded PDF to the input folder
        input_folder = "input"
        os.makedirs(input_folder, exist_ok=True)
        file_path = os.path.join(input_folder, file.filename)
        
        with open(file_path, "wb") as f:
            f.write(await file.read())
        
        print(f"File {file.filename} uploaded successfully.")

        # Extract text from the PDF
        print("=== Extracting text from PDF ===")
        pdf_texts = extract_pdfs_from_folder(input_folder)
        
        # Clean up the extracted texts
        print("\n=== Transforming extracted texts ===")
        clean_texts = transform_extracted_texts(pdf_texts)
        
        # Save the cleaned texts (if necessary)
        print("\n=== Saving processed texts ===")
        saved_files = load_texts(clean_texts)
        
        # Extract financial data from the cleaned text
        print("\n=== Extracting financial metrics ===")
        all_financial_data = []

        for text in clean_texts.values():
            financial_data = get_financial_data(text)
            if financial_data:
                all_financial_data.extend(financial_data)
        
        # Transform the financial data to prepare it for saving
        print("\n=== Transforming financial data ===")
        prepared_data = prepare_data_for_saving(all_financial_data)
        
        # Save the financial data to CSV
        print("\n=== Saving financial metrics ===")
        saved_data = save_data_to_csv(prepared_data)
        
        # Generate the stock purchase recommendation
        print("\n=== Getting Stock Purchase Recommendation ===")
        if saved_data.empty:
            return JSONResponse(content={"message": "No financial data available for recommendation."}, status_code=400)
        
        recommendation = stock_purchase_recommendation(saved_data)
        
        # Clean up the folders to save memory
        print("\n=== Cleaning up folders ===")
        # clean_up_folders(['input', 'output', 'datasets'])
        clean_up_folders(['output'])

        return JSONResponse(content=recommendation, status_code=200)

    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"message": str(e)}, status_code=500)

def clean_up_folders(folders):
    try:
        for folder in folders:
            # Check if the folder exists
            if os.path.exists(folder):
                # Iterate over the files in the folder
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    # Check if it is a file or directory
                    if os.path.isfile(file_path):
                        os.remove(file_path)  # Delete the file
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Delete the directory
                print(f"Cleaned up: {folder}")
            else:
                print(f"Folder not found: {folder}")
    except Exception as e:
        print(f"Error during cleanup: {e}")

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

    # Get stock purchase recommendation based on the financial data
    print("\n=== Getting Stock Purchase Recommendation ===")
    if saved_data.empty:
        print("No financial data available for recommendation.")
        return
    
    # Generate a recommendation based on the financial data
    recommendation = stock_purchase_recommendation(saved_data)
    print("\n=== Stock Purchase Recommendation ===")
    print(recommendation)

    # Clean up the folders to save memory
    print("\n=== Cleaning up folders ===")
    # clean_up_folders(['input', 'output', 'datasets'])
    clean_up_folders(['output'])

# Only run the program if we run this file directly
if __name__ == "__main__":
    main()