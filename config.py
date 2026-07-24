import os
import streamlit as st
from google import genai

try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except:
    API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY missing")

client = genai.Client(api_key=API_KEY)