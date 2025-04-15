import streamlit as st

from constants import FEATURE_OPTIONS
from utils import merge, split


def display_header_and_features() -> str:
    # Branding and Header
    st.set_page_config(page_title='PDF Toolkit', page_icon='📃')
    st.title("PDF Toolkit")

    # Sidebar and Feature Selections
    features = st.sidebar.selectbox(
        label='select a feature',
        options=FEATURE_OPTIONS,
    )
    return features


def handle_feature(feature_name: str) -> None:
    # Handling Merge PDF
    if feature_name == 'Select an Option':
        st.warning('Please select a valid feature.')

    if feature_name == 'Merge PDFs':
        st.subheader('Merge PDFs')
        files: list = st.file_uploader('Upload Multiple PDFs', accept_multiple_files=True, type=['pdf'])

        if st.button('Merge'):
            if files is not None:
                pass
            else:
                st.warning('Please upload at least two PDFs')

    # Handling Split PDF
    elif feature_name == 'Split PDF':
        st.subheader('Split PDF')
        file = st.file_uploader('Upload PDF', type=['pdf'])
        pages = st.text_input('Enter page range to split: eg.(1-3)')
        if st.button('Split'):
            if file and pages:
                pass
            else:
                st.warning('Please upload a PDF File and specify page range(1-3) to split')


def footer() -> None:
    st.markdown('---')
    st.caption('PDF Toolkit | ©️ Yash | Powered by Python and Streamlit')


def main() -> None:
    feature: str = display_header_and_features()
    handle_feature(feature)
    footer()


if __name__ == '__main__':
    main()
