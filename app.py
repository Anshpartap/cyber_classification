import streamlit as st
import tempfile
import os
from classify import classify_document

st.set_page_config(page_title="Cyber Document Classifier", layout="centered")
st.title("📄 Cyber Document Classifier")
st.write("Upload one or more PDF/DOCX files. The model will classify them as Sensitive or Normal.")

uploaded_files = st.file_uploader("Choose files", type=["pdf", "docx"], accept_multiple_files=True)
threshold = st.slider("Select Sensitivity Threshold", 0.0, 1.0, 0.6)

if uploaded_files:
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        result, prob = classify_document(tmp_path, threshold)
        st.success(f"**{uploaded_file.name}** → `{result}` (Probability: {prob:.2f})")
        os.unlink(tmp_path)
