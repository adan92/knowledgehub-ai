import streamlit as st

from services import DocumentService, KnowledgeHubService
from ui.chat import render_chat
from ui.sidebar import render_sidebar
from ui.styles import load_styles

from utils.path_utils import get_documents_path
from dotenv import load_dotenv

load_dotenv()


def main():

    st.set_page_config(
        page_title="KnowledgeHub AI",
        page_icon="🧠",
        layout="wide"
    )

    load_styles()

    document_service = DocumentService(
        get_documents_path()
    )

    knowledgehub = KnowledgeHubService()

    render_sidebar(document_service)

    render_chat(knowledgehub)


if __name__ == "__main__":
    main()
