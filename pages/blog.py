import streamlit as st

def show():
    st.title("Blog")
    st.image("resources/images/example.jpg", caption="Climbing Picture")
    password = st.text_input("Enter Password", type="password")

    if password == "your_password":
        st.write("Blog content here")
    else:
        st.write("Please enter the correct password to access the blog.")