2.) LLM RAG System (PDF-Based)

Overview:
This is a Retrieval-Augmented Generation (RAG) system built using Python that lets users ask questions about a PDF and receive answers grounded only in that document. The main goal is reliability: the model should answer from retrieved context, not from unsupported assumptions or it's internal billions of parameters.

Features:
- Query a PDF document interactively from the terminal
- Use semantic search through embeddings (HuggingFace)
- Retrieve relevant chunks using vector similarity (ChromaDB)
- Generate answers using an LLM (Groq with LLaMA 3)
- Reduce hallucination risk with strict prompt instructions

System Flow:
PDF -> Text Extraction -> Chunking -> Embeddings -> Vector Storage -> Retrieval -> LLM -> Answer

Tech Stack:
Python, LangChain, HuggingFace Embeddings (sentence-transformers), ChromaDB, Groq API (LLaMA 3), dotenv

How It Works:
The system first loads a PDF and splits the content into smaller chunks. Each chunk is converted into embeddings and stored in a vector database. When a user asks a question, the retriever finds the most relevant chunks and only that context is passed to the LLM. The model is explicitly instructed to answer only from the retrieved text.

Key Observation (Important):
During testing, when I asked:
"Tell me about the basis for Quantum Mechanics..."

the system responded:
"I don't know."

This happened because that specific information was not present in Quantum Computing.pdf.

This confirms:
- The RAG pipeline is working correctly
- The LLM did not rely on internal/background knowledge
- The system avoided hallucination and stayed grounded in source data

This behavior is intentional and important for real-world AI systems where factual reliability matters and this proved my RAG implementation was successful.

Example Use Cases:
- Research paper analysis
- Document-based Q&A systems
- AI assistants grounded in private/internal data

Limitations:
- Answer quality depends on retrieval quality
- The system cannot answer beyond the provided document
- No memory across sessions

Scope for Future Improvements:
- Add multi-document support
- Improve retrieval ranking
- Add a web-based UI
- Integrate a memory layer
