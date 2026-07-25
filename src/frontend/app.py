import streamlit as st

from api import ChatClient
from api.document_client import DocumentClient
from ui.about import render_about
from ui.chat import render_chat
from ui.documents import render_documents
from ui.sidebar import render_sidebar
from ui.styles import load_styles


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

    document_client = DocumentClient()
    chat_client = ChatClient()
    render_sidebar(document_client)
 
    if st.session_state.view == "chat":
        render_chat(chat_client)
    elif st.session_state.view == "knowledge":
        render_documents(document_client)
    elif st.session_state.view == "about":
        render_about()


if __name__ == "__main__":
    main()
