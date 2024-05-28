import streamlit as st

def show():
    st.title("Projects")
    st.write("Overview of projects")

    if st.button("Project 1"):
        show_project("Project 1", "Introduction to Project 1", "Results of Project 1", "Acknowledgment for Project 1")
        
    if st.button("Project 2"):
        show_project("Project 2", "Introduction to Project 2", "Results of Project 2", "Acknowledgment for Project 2")

def show_project(header, introduction, results, acknowledgment):
    st.header(header)
    st.write("### Introduction")
    st.write(introduction)
    st.write("### Results")
    st.write(results)
    st.write("### Acknowledgment")
    st.write(acknowledgment)