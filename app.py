import streamlit as st
from classify import classify_document
import tempfile
import os

st.set_page_config(page_title="Cyber Document Classifier")

st.title("🛡️ Cyber Document Classifier")
st.write("Upload PDF or DOCX files to classify them as **Sensitive** or **Normal**.")

# Upload files
uploaded_files = st.file_uploader("Upload file(s)", type=["pdf", "docx"], accept_multiple_files=True)

# Set threshold
threshold = st.slider("Select Sensitivity Threshold", 0.0, 1.0, 0.6, 0.01)

# On submission
if st.button("🔍 Classify Documents"):
    if not uploaded_files:
        st.warning("⚠️ Please upload at least one document.")
    else:
        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name

            category, prob = classify_document(open(tmp_path, "rb"), threshold)

            st.markdown("---")
            st.write(f"📄 **{uploaded_file.name}**")
            st.write(f"🧠 **Category:** {category}")
            st.write(f"🔢 **Probability:** {prob:.2f}")

            os.remove(tmp_path)
