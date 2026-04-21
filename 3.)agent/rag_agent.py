# rag_agent.py

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma


def build_vector_store(pdf_path: Path):
    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    docs = text_splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma.from_documents(docs, embedding)


def rag_agent(query, vectorstore):
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n".join(doc.page_content for doc in docs)
    return context