
import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Streamlit + Frontend App", layout="wide")

st.title("🚀 Integrated Streamlit + Vite Frontend")

html_file_path = os.path.join("dist", "index.html")

# Check if the frontend build exists
if os.path.exists(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    components.html(html_content, height=800, scrolling=True)
else:
    st.error("Frontend build not found. Please ensure 'dist/index.html' exists.")
