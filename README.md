# Financial Statement ETL Pipeline
As the first step in developing the stock recommendation feature for the Domma (Dompet Mahasiswa) app, I start by creating a simple Python ETL pipeline. This pipeline converts PDFs to text and then transforms the plain text into a CSV format for advanced analysis, with the resulting CSV used to build clustering and classification models. The goal of this project is to provide stock recommendations based on financial data, using a classification model to determine whether a stock is worth buying or not.

## Prerequisites
- Python 3.8+
- Tesseract OCR engine
- Poppler utilities

### System Dependencies Installation

#### Arch Linux
```bash
sudo pacman -S tesseract
sudo pacman -S poppler
```

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr
sudo apt-get install -y poppler-utils
```

#### macOS
```bash
brew install tesseract
brew install poppler
```

## Setup
1. Create a virtual environment (recommended):
```bash
python -m venv .venv # windows
# or
python3 -m venv .venv # linux

source .venv/bin/activate  
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Place financial statement PDF files in the `input` directory or create it first on root level
2. Run the pipeline:
```bash
python main.py 
# or
python3 main.py
```
3. Find the extracted text in the `output` directory


## Features
- Handles both regular PDFs and scanned PDFs
- OCR support for image-based PDFs
- Progress tracking with tqdm
- Error handling and logging
- Parallel processing for better performance 

## Contributor
[Falah Mandira Irawan](https://www.dicoding.com/users/falah_mandira_irawan/academies)