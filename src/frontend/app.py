import streamlit as st
from dotenv import load_dotenv

from core.services import DocumentService
from core.utils.path_utils import get_documents_path

from ui.chat import render_chat
from ui.documents import render_documents
from ui.sidebar import render_sidebar
from ui.styles import load_styles

load_dotenv()


def initialize_session():

    defaults = {
        "view": "chat"
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def main():

    st.set_page_config(
        page_title="KnowledgeHub AI",
        page_icon="🧠",
        layout="wide"
    )

    load_styles()

    initialize_session()

    document_service = DocumentService(
        get_documents_path()
    )

    render_sidebar(document_service)

    if st.session_state.view == "chat":
        render_chat()

    elif st.session_state.view == "knowledge":
        render_documents()


if __name__ == "__main__":
    main()