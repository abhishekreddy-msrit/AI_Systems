AI Systems
This repo contains a series of projects I am working on in building AI Systems from first principles.

Research Focus:
Agentic AI systems and autonomous intelligent platforms combining LLM reasoning with real-world systems.

Overview:
This repository documents my journey of building AI systems from first principles. The goal is to understand how modern AI applications are designed, structured, and deployed, not just use APIs.

Current Progress:
1. LLM Text Summarizer
A Python-based summarization system that generates structured outputs in short, detailed, and technical modes using prompt engineering and LLM APIs.
Focus: Prompt control and structured output generation.

2. PDF-based RAG System
A Retrieval-Augmented Generation system that allows querying a PDF document and generates answers strictly grounded in the document content.
Focus: Embeddings, vector search, retrieval pipelines, and hallucination control.

Key Learnings:
1. Understanding how LLMs behave under prompt constraints
2. Difference between model knowledge and retrieved knowledge
3. Importance of embeddings for semantic search
4. How chunking impacts retrieval quality
5. Designing systems that avoid hallucination

Important Observation:
During testing, the system correctly responded with "I don't know" when the answer was not present in the document. This confirmed that the model was restricted to retrieved context and did not hallucinate and the rag implementation was successful from 2.).

Tech Stack:
Python
Groq API (LLaMA 3)
LangChain
HuggingFace Embeddings (sentence-transformers)
ChromaDB
dotenv

Repository Structure(Current status quo):
01_text_summarizer
02_rag_system

Next Steps:
1. Build agent-based systems
2. Add memory and multi-step reasoning
3. Expand to multi-document RAG
4. Integrate AI systems with robotics
