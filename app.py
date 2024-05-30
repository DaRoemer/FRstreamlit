import streamlit as st
from pages import home, cv_references, projects, blog, legal
from resources.translations import translate

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "CV and References", "Projects", "Blog", "Legal"])
    
    st.sidebar.title("Language")
    language = st.sidebar.radio("Switch Language", ["English", "German"])
    st.write(f"Selected Language: {language}")

    if page == "Home":
        home.show()
    elif page == "CV and References":
        cv_references.show()
    elif page == "Projects":
        projects.show()
    elif page == "Blog":
        blog.show()
    elif page == "Legal":
        legal.show()


if __name__ == "__main__":
    main()
