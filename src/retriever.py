from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_retriever(index_path="index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    db = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    return db.as_retriever()
