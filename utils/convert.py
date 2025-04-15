from uuid import uuid4
from streamlit.runtime.uploaded_file_manager import UploadedFile
from PIL import Image
import streamlit as st
import fitz


def convert_pdf_to_image(pdf_file: UploadedFile):
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

        for i, page in enumerate(doc):
            pix = page.get_pixmap(dpi=200)
            img_filename = f"output/convert/image/Converted_page_{i + 1}.png"
            pix.save(img_filename)

            with open(img_filename, 'rb') as f:
                st.download_button(
                    label=f"Download image {i + 1}",
                    data=f,
                    file_name=img_filename,
                    mime='image/png',
                )
        st.success('PDF converted to image successfully using PyMuPDF!')

    except Exception as e:
        st.error(f"An error Occurred: {str(e)[:100]}")


def convert_image_to_pdf(image_path: UploadedFile):
    try:
        image = Image.open(image_path)
        pdf_filename = f'output/convert/pdf/converted_output-{uuid4()}.pdf'
        image.convert('RGB').save(pdf_filename)

        # provide link to download
        with open(pdf_filename, 'rb') as f:
            st.download_button(
                label='Download converted PDF',
                data=f,
                file_name=pdf_filename,
                mime='application/pdf',
            )
        st.success('Image converted to PDF successfully!')

    except Exception as e:
        st.error(f"An error Occurred: {str(e)[:100]}")
