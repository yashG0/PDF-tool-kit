from streamlit.runtime.uploaded_file_manager import UploadedFile
from PyPDF2 import PdfMerger
import streamlit as st
import os


def merge_pdfs(files: list[UploadedFile]) -> None:
    output_path = "output/merge"
    os.makedirs(output_path, exist_ok=True)

    # Save the output file
    output_filename: str = os.path.join(output_path, "merged_output.pdf")

    try:
        merger = PdfMerger()
        for file in files:
            merger.append(file)

        merger.write(output_filename)
        merger.close()

        with open(output_filename, 'rb') as f:
            st.download_button(
                label="Download Merged PDF",
                data=f,
                file_name=output_filename,
                mime='application/pdf',
            )
            st.success("PDF Merged Successfully")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
