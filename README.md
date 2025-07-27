# Cyprus Legal RAG Agent

A Retrieval-Augmented Generation (RAG) assistant for answering legal questions using information from uploaded documents. The system uses modern NLP techniques to chunk, embed, index, retrieve, and answer questions, with a simple web interface for user interaction.

## Features
- Upload and process legal documents (PDFs)
- Chunk and embed text for efficient retrieval
- Use FAISS for fast vector search
- Answer questions using Google Gemini LLM, strictly based on document context
- Simple Gradio web UI
- Greek language support

## Project Structure
```
app.py                # Main entry point
requirements.txt      # Python dependencies
src/
  loader.py           # Loads and reads documents
  chunker.py          # Splits text into chunks
  embedder.py         # Embeds and stores chunks in FAISS index
  retriever.py        # Loads retriever for searching chunks
  rag_agent.py        # RAG chain and LLM integration
  ui.py               # Gradio web interface
index/                # FAISS index and metadata
  index.faiss
  index.pkl
data/                 # Source documents (PDFs)
.env                  # API keys and secrets (not tracked in git)
```

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Add your Gemini API key to `.env`:**
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. **Add your legal documents (PDFs) to the `data/` folder.**

## Usage
Run the application:
```
python app.py
```
This will launch a Gradio web interface (default: http://localhost:7860) where you can ask legal questions in Greek.

## Deployment
- The Gradio UI is suitable for prototyping and internal use.
- For production, consider Docker, cloud VM, or PaaS deployment.
- Use a reverse proxy (e.g., Nginx) for custom domains and HTTPS.


## License
Specify your license here.

## Acknowledgements
- [LangChain](https://github.com/langchain-ai/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [Gradio](https://gradio.app/)
- [Google Gemini](https://ai.google.dev/)
