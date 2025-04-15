import os
from streamlit.runtime.uploaded_file_manager import UploadedFile
import pikepdf
import streamlit as st


def compress_pdf_file(pdf_file: UploadedFile, level: int) -> None:
    output_path = "output/compress"
    os.makedirs(output_path, exist_ok=True)

    # Save the output file
    output_filename: str = os.path.join(output_path, "compressed_output.pdf")

    try:
        input_pdf = pikepdf.Pdf.open(pdf_file)

        # Save with optimization (not direct compression, but it optimizes objects and streams)
        input_pdf.save(
            output_filename,
            compress_streams=True  # Compresses PDF streams (like images and text)
        )

        with open(output_filename, "rb") as f:
            st.download_button(
                label="Download Compressed PDF",
                data=f,
                file_name="compressed.pdf",
                mime="application/pdf"
            )

        st.success("PDF compressed successfully!")

    except Exception as e:
        st.error(f"An error occurred: {str(e)[:100]}")
