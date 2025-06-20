
import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Streamlit + Frontend App", layout="wide")

st.title("🚀 Integrated Streamlit + Vite Frontend")

# Render HTML with proper styling and clickable text links
st.markdown("""
<style>
.contact-info {
    font-family: Arial, sans-serif;
    margin-bottom: 20px;
}
.contact-item {
    margin-bottom: 10px;
}
.contact-label {
    font-weight: bold;
    width: 140px;
    display: inline-block;
}
.social-links {
    margin-top: 20px;
}
.social-link {
    margin-right: 15px;
    text-decoration: none;
    font-weight: bold;
    color: #1f77b4;
}
</style>

<div class="contact-info">
  <div class="contact-item">
    <span class="contact-label">Email:</span>
    <span>manmohan.rawat@gmail.com</span>
  </div>
  <div class="contact-item">
    <span class="contact-label">Phone:</span>
    <span>+91 9916225795</span>
  </div>
  <div class="contact-item">
    <span class="contact-label">Location:</span>
    <span>New Delhi, India</span>
  </div>
  <div class="contact-item">
    <span class="contact-label">Experience:</span>
    <span>22 Years • Design & Development</span>
  </div>
</div>

<div class="social-links">
  <a href="https://linkedin.com/in/manmohanrawat" class="social-link" target="_blank">LinkedIn Profile</a>
  <a href="https://incomparable-unicorn-cb5a02.netlify.app" class="social-link" target="_blank">Personal Website</a>
</div>
""", unsafe_allow_html=True)


html_file_path = os.path.join("dist", "index.html")

# Check if the frontend build exists
if os.path.exists(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    components.html(html_content, height=800, scrolling=True)
else:
    st.error("Frontend build not found. Please ensure 'dist/index.html' exists.")
