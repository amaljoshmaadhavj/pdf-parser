# PDF Parser (Streamlit App)
A simple Streamlit-based web application that extracts text from each page of a PDF file and allows users to download the extracted content as text files.

## Features
- Upload PDF files through a web interface
- Extract text page-by-page
- Preview extracted text
- Download extracted pages as a ZIP file

## Project Structure

```
pdf-parser/
├── app.py               # Streamlit application
├── pdf_reader.py        # Core PDF extraction logic (CLI)
├── requirements.txt     # Project dependencies
├── Extracted Pages/     # Output directory
├── .gitignore
└── README.md
```
## Requirements
- Python 3.x
- Streamlit
- PyPDF2

Install dependencies:
```bash
pip install -r requirements.txt
```

## Run Locally

```bash
streamlit run app.py
```

The app will be available at:
```
http://localhost:8501
```

## Usage
1. Upload a PDF file
2. Click **Extract Text**
3. Preview extracted text
4. Download all extracted pages as a ZIP file

## Notes
- Works with text-based PDFs
- Scanned PDFs require OCR (not included)

## Author
Amaljosh Maadhav J