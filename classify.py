import os
import pdfplumber 
import numpy as np
import torch
import docx
import PyPDF2
import joblib
from transformers import BertTokenizer, BertModel
from sklearn.feature_extraction.text import CountVectorizer

# === Load Models & Tokenizers ===
xgb_classifier = joblib.load("xgb_classifier (1).pkl")
lda_model = joblib.load("lda_model (2).pkl")
vectorizer = joblib.load("vectorizer (1).pkl")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
bert_model = BertModel.from_pretrained("bert-base-uncased")
bert_model.eval()

# === Utility: Extract Text from PDF or DOCX ===

def extract_text(file):
    text = ""
    try:
        if file.name.endswith(".docx"):
            doc = docx.Document(file)
            text = " ".join([para.text for para in doc.paragraphs])
        elif file.name.endswith(".pdf"):
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
    except Exception as e:
        print(f"❌ Error reading file: {e}")
    return text.strip()
    

# === Feature: Get BERT Embedding ===
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    return outputs.last_hidden_state[:, 0, :].numpy().flatten()

# === Feature: Get LDA Topic Distribution ===
def get_lda_features(text):
    text_vector = vectorizer.transform([text])
    return lda_model.transform(text_vector).flatten()

# === Classify a Document ===
def classify_document(file, threshold=0.6):
    text = extract_text(file)
    if not text:
        return "Unreadable", 0.0

    bert_feat = get_bert_embedding(text).reshape(1, -1)
    lda_feat = get_lda_features(text).reshape(1, -1)
    features = np.hstack((bert_feat, lda_feat))

    probability = xgb_classifier.predict_proba(features)[0][1]
    category = "Sensitive" if probability >= threshold else "Normal"

    return category, probability
