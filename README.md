AI Systems — Learning by Building

This repository documents my journey of building AI systems from scratch, focusing on practical understanding of LLMs, RAG pipelines, and agent-based architectures.

Instead of just learning theory, each module here is an implementation-first approach to understanding how modern AI systems actually work.


Current Progress

Recent Update:
Encountered a model deprecation issue during runtime while using Groq.
Updated the system to a supported model and validated the fix through runtime testing.

1) Text Summarizer Script
A simple LLM-powered summarization tool built using Groq API.

What it does:
- Accepts raw text input from terminal
- Supports multiple summarization styles (short, detailed, technical)
- Demonstrates prompt engineering and API integration

Key Learning:
Understanding how LLMs behave based on prompt structure.


2) RAG (Retrieval-Augmented Generation)

A document-based question-answering system built using:
- LangChain
- HuggingFace embeddings
- Chroma vector database

What it does:
- Loads PDF documents
- Splits them into chunks
- Converts text into embeddings
- Retrieves relevant context based on query
- Uses LLM only on retrieved data

Key Highlight:
The system correctly refuses to answer when the information is not present in the document.

Example:
When asked something outside the PDF context, the model responded:
"I don't know"

This confirms:
- No hallucination
- Proper retrieval-based grounding

Key Learning:
Understanding how to control LLM behavior using external knowledge instead of relying on model memory.


3) AI Agent (Work in Progress)

A basic agent system that:
- Takes user input
- Uses LLM-based intent planning
- Routes queries dynamically across summarization, explanation, and research agents
- Includes a verification step to keep responses grounded in retrieved context

Current State:
- Dynamic multi-agent routing implemented
- Verification flow added for reliability checks

Next Steps:
- Add multi-step reasoning (ReAct pattern)
- Add multiple tools (RAG + summarizer + others)
- Build decision-making loop

Key Learning:
Difference between:
- Simple scripts
- Tool-based systems
- True AI agents


Tech Stack

- Python
- Groq API (llama-3.3-70b-versatile)
- LangChain
- HuggingFace Sentence Transformers
- ChromaDB
- dotenv



Project Philosophy

This repo is not about perfect projects.
It is about building real systems step by step and understanding:

- How LLMs actually work
- Where they fail
- How to control them
- How to turn them into usable systems

Each folder represents a step toward building production-level AI systems.


Upcoming Work

- Multi-tool AI Agent (Planner + Executor)
- Memory-enabled agents
- Autonomous workflows
- Integration with real-world systems


Goal

To reach a level where I can build end-to-end AI systems combining:

- LLM reasoning
- Retrieval systems
- Agentic workflows
- Real-world applications


Author

Abhishek Reddy T