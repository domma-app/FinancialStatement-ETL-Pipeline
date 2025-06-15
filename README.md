# Stock Purchase Recommendation App
This app analyzes financial statements extracted from PDF files and provides a stock purchase recommendation in the form of a percentage score. Using an ETL pipeline, the app processes raw financial data from financial statement (PDF), transforms it into a structured format, and applies machine learning models to predict the likelihood of a stock being a good investment. The result is a percentage score indicating the confidence level of the recommendation, helping investors make data-driven decisions.

## Prerequisites
- Python 3.8 - 3.11 (3.10 is recommended),
- Tesseract OCR engine,
- Poppler utilities.

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
1. Place financial statement PDF files in the `input` directory or create it first on project level
2. Run the pipeline:
```bash
python main.py 
# or
python3 main.py
```
3. Find the extracted text in the `output` directory


## Features
- Provides stock purchase recommendations expressed as percentage scores,
- Returns financial metrics such as ROE, ROA, D/E Ratio, Equity Ratio, A/E Ratio, and Leverage,
- Handles both regular PDFs and scanned PDFs,
- OCR support for image-based PDFs,
- Progress tracking with tqdm,
- Error handling and logging,
- Parallel processing for better performance.

## Contributor
[Falah Mandira Irawan](https://www.dicoding.com/users/falah_mandira_irawan/academies)