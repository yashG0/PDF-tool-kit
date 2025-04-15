from uuid import uuid4

from streamlit.runtime.uploaded_file_manager import UploadedFile
import pikepdf
import streamlit as st


def compress_pdf_file(pdf_file: UploadedFile, level: int) -> None:
    input_pdf = pikepdf.Pdf.open(pdf_file)

    # Save with optimization (not direct compression, but it optimizes objects and streams)
    output_filename = f"output/compress/compressed_{uuid4()}.pdf"

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
