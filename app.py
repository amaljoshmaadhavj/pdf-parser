import streamlit as st
import os
from pathlib import Path
import PyPDF2
import zipfile


def extract_pdf_pages_to_text(pdf_file, output_dir="Extracted Pages"):
    """
    Extract text from each page of an uploaded PDF
    and save each page as a separate .txt file.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    reader = PyPDF2.PdfReader(pdf_file)
    total_pages = len(reader.pages)

    extracted_files = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        file_path = Path(output_dir) / f"page_{page_number}.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

        extracted_files.append(file_path)

    return total_pages, extracted_files


def zip_output_files(files, zip_name="extracted_pages.zip"):
    """
    Zip extracted text files for download.
    """
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, arcname=file.name)
    return zip_name


# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="PDF Parser", page_icon="📄")

st.title("📄 PDF Parser")
st.write("Upload a PDF file to extract text from each page.")

uploaded_pdf = st.file_uploader(
    "Upload a PDF file", type=["pdf"]
)

if uploaded_pdf:
    st.success("PDF uploaded successfully!")

    if st.button("Extract Text"):
        with st.spinner("Extracting text from PDF..."):
            pages, files = extract_pdf_pages_to_text(uploaded_pdf)

            zip_file = zip_output_files(files)

        st.success(f"Extraction completed! Total pages: {pages}")

        st.download_button(
            label="⬇️ Download Extracted Text (ZIP)",
            data=open(zip_file, "rb"),
            file_name=zip_file,
            mime="application/zip"
        )

        st.subheader("Preview (First Page)")
        with open(files[0], "r", encoding="utf-8") as f:
            st.text_area(
                label="Extracted Text",
                value=f.read(),
                height=300
            )