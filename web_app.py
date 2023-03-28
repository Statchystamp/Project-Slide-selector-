from pathlib import Path
import streamlit as st
from PIL import Image


PAGE_TILTE = "NLP Keyword Search Model"

st.set_page_config(page_title = PAGE_TILTE)
st.title ("Project Slide Searcher")

user_input = st.text_input("Enter Keywords here: ")