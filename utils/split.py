import os
from PyPDF2 import PdfReader, PdfWriter
from streamlit.runtime.uploaded_file_manager import UploadedFile
import streamlit as st


def split_pdfs(file: UploadedFile, pages: str) -> None:
    output_path = "output/spit"
    os.makedirs(output_path, exist_ok=True)

    # Save the output file
    output_filename: str = os.path.join(output_path, "split_output.pdf")

    try:
        pdf_reader = PdfReader(file)

        page_range = pages.split("-")
        start_page = int(page_range[0]) - 1
        end_page = int(page_range[1]) if len(page_range) > 1 else None

        pdf_writer = PdfWriter()
        for page in range(start_page, end_page or len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

        # saving the split file

        with open(output_filename, "wb") as output_file:
            pdf_writer.write(output_file)

        # provide download link
        with open(output_filename, "rb") as f:
            st.download_button(
                label="Download Split PDF",
                data=f,
                file_name=output_filename,
                mime="application/pdf",
            )
            st.success("PDF Split Successfully")

    except IndexError:
        st.error("Invalid PDF range specified!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}!")
