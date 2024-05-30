import streamlit as st
from resources.translations import translate


def show():
    language = st.session_state.get("language")

    st.title(translate("Legal", language))
    st.header(translate("Terms", language))
    st.write(translate("Terms content here", language))

    st.header(translate("Privacy Policy", language))
    st.write(translate("Privacy policy content here", language))