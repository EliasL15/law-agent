from langchain.chains import RetrievalQA
from langchain.llms.base import LLM
from typing import Optional, List
from pydantic import BaseModel
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
import os
from dotenv import load_dotenv

custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""Χρησιμοποίησε μόνο τις παρακάτω πληροφορίες για να απαντήσεις στην ερώτηση. 
Μην προσθέτεις εξωτερική γνώση. Αν δεν υπάρχει αρκετή πληροφορία, πες "Δεν υπάρχουν επαρκή στοιχεία στο έγγραφο."

{context}

Ερώτηση: {question}
Απάντηση στα ελληνικά:"""
)

def load_gemini_llm(api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    def run_llm(prompt):
        response = model.generate_content(prompt)
        return response.text.strip()

    return run_llm

class GeminiWrapper(LLM, BaseModel):
    gemini_fn: callable

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        return self.gemini_fn(prompt)

    @property
    def _llm_type(self) -> str:
        return "google-gemini"

def build_rag_chain(retriever):
    load_dotenv()
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    gemini_fn = load_gemini_llm(api_key=gemini_api_key)
    llm = GeminiWrapper(gemini_fn=gemini_fn)

    # Use custom prompt with the retriever
    qa_chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=custom_prompt)
    return RetrievalQA(combine_documents_chain=qa_chain, retriever=retriever)
