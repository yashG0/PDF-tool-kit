from streamlit.runtime.uploaded_file_manager import UploadedFile
import streamlit as st
from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO
import os


def protect_pdf(pdf_file: UploadedFile, passwd: str) -> None:
    # Ensure output folder exists
    output_path = "output/protect"
    os.makedirs(output_path, exist_ok=True)

    # Save the output file
    output_filename: str = os.path.join(output_path, "protected_output.pdf")

    try:
        pdf_reader = PdfReader(pdf_file)
        pdf_writer = PdfWriter()

        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        pdf_writer.encrypt(passwd)

        # Create a BytesIO buffer to store the encrypted PDF
        pdf_buffer = BytesIO()
        pdf_writer.write(pdf_buffer)
        pdf_buffer.seek(0)

        with open(output_filename, "wb") as f:
            st.download_button(
                label="Download Protected PDF",
                data=pdf_buffer,
                file_name=output_filename,
                mime="application/pdf",
            )
        st.success("PDF Protected Successfully!")

    except Exception as e:
        st.error(f"An error occurred: {e}")
