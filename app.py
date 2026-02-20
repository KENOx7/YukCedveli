import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ağıllı Dərs Cədvəli",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Read the HTML content
try:
    with open("timetable_ui.html", "r", encoding="utf-8") as f:
        html_code = f.repr_html = f.read()
except FileNotFoundError:
    html_code = "Error: timetable_ui.html not found in the deployment directory."

# Render the HTML file inside Streamlit using an iframe
# We give it a large height so the internal scrolling of the UI handles the overflow
components.html(html_code, height=900, scrolling=True)
