from uuid import uuid4

from streamlit.runtime.uploaded_file_manager import UploadedFile
import fitz
import streamlit as st
import os
from PIL import Image
import io


def make_image_transparent(image_data: bytes, alpha: float = 0.3) -> bytes:
    image = Image.open(io.BytesIO(image_data)).convert("RGBA")
    r, g, b, a = image.split()
    a = a.point(lambda p: int(p * alpha))  # reduce alpha
    image.putalpha(a)

    output = io.BytesIO()
    image.save(output, format="PNG")
    return output.getvalue()


def add_watermark(pdf: UploadedFile, watermark: UploadedFile) -> None:
    output_path = "output/watermark"
    os.makedirs(output_path, exist_ok=True)

    # Save the output file
    output_filename: str = os.path.join(output_path, "watermark_output.pdf")

    try:
        pdf_doc = fitz.open(stream=pdf.read(), filetype="pdf")

        watermark_stream = make_image_transparent(watermark.read(), alpha=0.3)
        watermark_rect = fitz.Rect(50, 50, 500, 500)

        for page in pdf_doc:
            page.insert_image(
                watermark_rect,
                stream=watermark_stream,
                overlay=True,
                keep_proportion=True,
            )

        # save the watermark PDF
        pdf_doc.save(output_filename)

        # provide download link for the watermark PDF
        with open(output_filename, 'rb') as f:
            st.download_button(
                label="Download watermark",
                data=f,
                file_name=output_filename,
                mime="application/pdf",
            )
            st.success("watermark Applied successfully!")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
