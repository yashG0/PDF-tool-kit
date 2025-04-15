import fitz  # PyMuPDF
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


def extract_text_from_pdf(file: UploadedFile) -> None:
    """Extracts text from the uploaded PDF file."""
    try:
        # Open the PDF
        pdf_document = fitz.open(stream=file.read(), filetype="pdf")
        extracted_text = ""

        # Loop through all pages and extract text
        for page in pdf_document:
            extracted_text += page.get_text("text") + "\n\n"

        # Display extracted text
        if extracted_text.strip():
            st.text_area("Extracted Text:", extracted_text, height=300)
            # Provide an option to download as a text file
            st.download_button(
                label="Download Extracted Text",
                data=extracted_text,
                file_name="extracted_text.txt",
                mime="text/plain"
            )
            st.success("Text extracted successfully!")
        else:
            st.warning("No text found in the PDF.")

    except Exception as e:
        st.error(f"An error occurred while extracting text: {e}")
