import streamlit as st

def show():
    st.title("CV and References")
    st.write("Top general description")

    with open("resources/cv_and_references.zip", "rb") as file:
        st.download_button(label="Download CV and References", data=file, file_name="cv_and_references.zip")

    st.write("University details with images")
    # Add images and texts for each university
    st.image("resources/images/university1.jpg", caption="University 1")
    st.write("Short text about University 1")

    st.write("References")
    # Add references images
    st.image("resources/images/reference1.jpg", caption="Reference 1")