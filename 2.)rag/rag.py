import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma


def build_vector_store(pdf_path: Path) -> Chroma:
    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    docs = text_splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma.from_documents(docs, embedding)


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    env_candidates = [
        project_dir / ".env",
        project_dir / "env",
        project_dir.parent / ".env",
        project_dir.parent / "env",
        project_dir.parent / "1.)text_summarizer_script" / ".env",
        project_dir.parent / "1.)text_summarizer_script" / "env",
    ]
    for env_path in env_candidates:
        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
            break

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing GROQ_API_KEY. Add it to environment or create "
            f"{project_dir / '.env'} with GROQ_API_KEY=your_key_here"
        )

    model_name = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    client = Groq(api_key=api_key)

    pdf_path = project_dir / "Quantum Computing.pdf"
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    db = build_vector_store(pdf_path)

    while True:
        try:
            query = input("\nAsk a question (type 'exit' to quit):\n").strip()
        except EOFError:
            print("\nInput stream closed. Exiting.")
            break
        if query.lower() == "exit":
            break

        retrieved_docs = db.similarity_search(query, k=3)
        context = "\n".join(doc.page_content for doc in retrieved_docs)

        prompt = (
            "Answer the question using ONLY the context below.\n"
            "If the answer is not present, say \"I don't know\".\n\n"
            f"Context:\n{context}\n\n"
            f"Question:\n{query}"
        )

        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
        )

        print("\nAnswer:\n")
        print(response.choices[0].message.content)


if __name__ == "__main__":
    main()