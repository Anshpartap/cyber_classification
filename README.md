# 🔐 Cyber Document Classifier

A machine learning web application to classify uploaded documents (PDF/DOCX) as **Sensitive** or **Normal** based on their content, using NLP and ML techniques like **BERT**, **LDA**, and **XGBoost**.

🚀 **Live Demo**  
👉 [Streamlit App] https://cyberclassification-9dba9jfzgpgdpcuyjahqki.streamlit.app/

---

## 📂 Features

- ✅ Upload **single or multiple PDF/DOCX** documents
- ✅ Classify as **Sensitive** or **Normal** based on content
- ✅ Uses **BERT** embeddings + **LDA** topic features
- ✅ Trained using **XGBoost** with 85%+ accuracy
- ✅ No internet dependency for model loading (offline inference)

---

## 🧠 Model Architecture

- **Text Extraction** from PDF/DOCX
- **BERT** (`bert-base-uncased`) for deep contextual embeddings
- **LDA** (Latent Dirichlet Allocation) for topic modeling
- **Feature Fusion:** Combined BERT + LDA vectors
- **Classifier:** Trained XGBoost model with SMOTE resampling

---

## 🛠️ Tech Stack

| Component        | Tool/Library            |
|------------------|--------------------------|
| Text Embedding   | BERT (Transformers)      |
| Topic Modeling   | LDA (sklearn)            |
| Classification   | XGBoost                  |
| Web Interface    | Streamlit                |
| File Parsing     | PyPDF2 / python-docx     |

---

## 📝 How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/your-username/cyber-document-classifier.git
cd cyber-document-classifier
