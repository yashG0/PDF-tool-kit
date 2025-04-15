from streamlit.runtime.uploaded_file_manager import UploadedFile
from PIL import Image
import streamlit as st
import fitz
import os


def convert_pdf_to_image(pdf_file: UploadedFile):
    output_path = "output/image"
    os.makedirs(output_path, exist_ok=True)

    # Save the output file
    img_filename: str = os.path.join(output_path, "converted_output.pdf")

    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

        for i, page in enumerate(doc):
            pix = page.get_pixmap(dpi=200)
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
    output_path = "output/convert/pdf"
    os.makedirs(output_path, exist_ok=True)

    # Save the output file
    pdf_filename: str = os.path.join(output_path, "converted_output.pdf")

    try:
        image = Image.open(image_path)
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
