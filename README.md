# PDF Parser
A Python utility to extract text from each page of a PDF file and save every page as a separate `.txt` file.

## Features
- Page-wise text extraction from PDFs
- Automatic output directory creation
- Simple and easy-to-run script

## Project Structure

```
pdf-parser/
├── pdf_reader.py
├── requirements.txt
├── Extracted Pages/
│   ├── page_1.txt
│   ├── page_2.txt
│   └── ...
├── .gitignore
└── README.md
```
## Requirements
- PyPDF2

Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run
1. Place your PDF file in the project root
2. Update the file name in `pdf_reader.py` if needed
3. Run:
```bash
python pdf_reader.py
```

## Output
- Extracted text files are saved in the `Extracted Pages/` folder
- Each text file corresponds to one page of the PDF

## Notes
- Works with text-based PDFs
- Scanned PDFs require OCR (not included)


## Author
Amaljosh Maadhav J