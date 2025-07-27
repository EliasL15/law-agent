from src.loader import load_text_files
from src.chunker import chunk_text
from src.embedder import embed_and_store
from src.retriever import load_retriever
from src.rag_agent import build_rag_chain
from src.ui import launch_interface

texts = load_text_files()
all_chunks = []
for text in texts:
    all_chunks.extend(chunk_text(text))
embed_and_store(all_chunks)

retriever = load_retriever()
qa_chain = build_rag_chain(retriever)
launch_interface(qa_chain)
