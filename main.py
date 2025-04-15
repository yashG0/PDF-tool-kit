import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

from constants import FEATURE_OPTIONS
from utils import merge, split, watermark, convert, compress, extract,protect


def display_header_and_features() -> str:
    # Branding and Header
    st.set_page_config(page_title='PDF Toolkit', page_icon='📃')
    st.title("PDF Toolkit")
    st.badge('Enjoy')
    st.markdown('---')

    # Sidebar and Feature Selections
    features = st.sidebar.selectbox(
        label='Select a feature',
        options=FEATURE_OPTIONS,
    )
    return features


def handle_feature(feature_name: str) -> None:
    if feature_name == 'Select an Option':
        st.warning('Please select a valid feature.')

    # Handling Merge PDF
    if feature_name == 'Merge PDFs':
        st.subheader('Merge PDFs')
        files: list[UploadedFile] = st.file_uploader('Upload Multiple PDFs', accept_multiple_files=True, type=['pdf'])

        if st.button('Merge'):
            if files:
                merge.merge_pdfs(files)
            else:
                st.warning('Please upload at least two PDFs')

    # Handling Split PDF
    elif feature_name == 'Split PDF':
        st.subheader('Split PDF')
        file: UploadedFile = st.file_uploader('Upload PDF', type=['pdf'])
        pages: str = st.text_input('Enter page range to split: eg.(1-3)')
        if st.button('Split'):
            if file and pages:
                split.split_pdfs(file, pages)
            else:
                st.warning('Please upload a PDF File and specify page range(1-3) to split')

    # Handling watermark
    elif feature_name == 'Watermark PDF':
        st.subheader('Watermark PDF')
        file: UploadedFile = st.file_uploader('Upload PDF', type=['pdf'])
        watermark_image: UploadedFile = st.file_uploader("Upload Watermark Image", type=['png', 'jpg', 'jpeg'])
        if st.button('Apply Watermark'):
            if file and watermark_image:
                watermark.add_watermark(pdf=file, watermark=watermark_image)

            else:
                st.warning('Please upload both PDF and Watermark Images!')

    # Convert - PDF↔️Image
    elif feature_name == 'Convert - PDF↔️Image':
        st.subheader('Convert - PDF↔️Image')
        convertion_type = st.radio("Select Conversion Type", ["PDF to Image", "Image to PDF"])
        file = st.file_uploader('Upload PDF', type=['pdf', 'jpg', 'png', 'jpeg'])
        if st.button('Convert'):
            if file:
                if convertion_type == 'PDF to Image':
                    convert.convert_pdf_to_image(file)
                else:
                    convert.convert_image_to_pdf(file)
            else:
                st.warning('Please upload file to convert!')

    # Compress PDF
    elif feature_name == 'Compress PDF':
        st.subheader('Compress PDF')
        file = st.file_uploader('Upload PDF', type=['pdf'])
        compression_level = st.slider("Select Compression Level", min_value=1, max_value=5, value=2)
        if st.button('Compress'):
            if file:
                compress.compress_pdf_file(file, compression_level)
            else:
                st.warning('Please upload PDF to compress!')

    # Extract Text from PDF
    elif feature_name == 'Extract text':
        st.subheader('Extract text')
        file = st.file_uploader('Upload PDF', type=['pdf'])
        if st.button('Extract'):
            if file:
                extract.extract_text_from_pdf(file)
            else:
                st.warning('Please upload PDF to extract data!')

    # Protect PDF (LOCK)
    elif feature_name == 'Protect PDF':
        st.subheader('Protect PDF')
        file = st.file_uploader('Upload PDF', type=['pdf'])
        password = st.text_input('Enter password', type='password')
        if st.button('Protect PDF'):
            if file:
                protect.protect_pdf(file, password)
            else:
                st.warning('Please upload PDF and password!')


def footer() -> None:
    st.markdown('---')
    st.caption('PDF 📃 Toolkit | ©️ Yash | Powered by Python and Streamlit')


def main() -> None:
    feature: str = display_header_and_features()
    handle_feature(feature)
    footer()


if __name__ == '__main__':
    main()
