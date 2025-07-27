import os
import pdfplumber

def load_text_files(data_dir="data"):
    texts = []
    for file in os.listdir(data_dir):
        path = os.path.join(data_dir, file)
        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())
        elif file.endswith(".pdf"):
            with pdfplumber.open(path) as pdf:
                full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)
                texts.append(full_text)
    return texts
