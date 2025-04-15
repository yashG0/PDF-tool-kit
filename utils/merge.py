from streamlit.runtime.uploaded_file_manager import UploadedFile
from PyPDF2 import PdfMerger
import streamlit as st
from uuid import uuid4


def merge_pdfs(files: list[UploadedFile]) -> None:
    try:
        merger = PdfMerger()
        for file in files:
            merger.append(file)

        output_filename = f"output/merge/merged_pdf-{uuid4()}.pdf"
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
