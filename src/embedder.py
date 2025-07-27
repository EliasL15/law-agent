from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def embed_and_store(chunks, index_path="index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    db = FAISS.from_texts(chunks, embeddings)
    db.save_local(index_path)
