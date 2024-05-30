import streamlit as st

def show():
    st.title("Home")
    st.image("resources/images/example.jpg", caption="Your Picture")
    st.write("A few sentences about yourself.")
    st.markdown("[Link to CV and References](#)")
    st.markdown("[Link to Projects](#)")
    st.markdown("[Link to Blog](#)")
    st.markdown("[Link to ???](#)")