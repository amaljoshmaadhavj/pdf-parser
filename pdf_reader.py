# AMALJOSH MAADHAV J
import os
from pathlib import Path
import PyPDF2


def extract_pdf_pages_to_text(pdf_path: str, output_dir: str = "Extracted Pages") -> None:
    """
    Extract text from each page of a PDF and save each page
    as a separate .txt file.
    """

    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Check if PDF exists
    if not os.path.exists(pdf_path):
        print(f"PDF not found: {pdf_path} ❌")
        return

    try:
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            total_pages = len(reader.pages)

            print(f"Total pages found: {total_pages}\n 📄")

            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text() or ""

                output_file = Path(output_dir) / f"page_{page_number}.txt"
                with open(output_file, "w", encoding="utf-8") as txt_file:
                    txt_file.write(text)

                print(f"Extracted page {page_number} ✅")

        print("\nExtraction completed successfully! ")

    except Exception as e:
        print(f"Error while processing PDF: {e} ⚠️")


if __name__ == "__main__":
    pdf_file = "LordoftheFlies.pdf"
    extract_pdf_pages_to_text(pdf_file)