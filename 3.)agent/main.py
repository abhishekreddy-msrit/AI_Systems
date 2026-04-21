from groq import Groq
from dotenv import load_dotenv
import os
from pathlib import Path

from orchestrator_agent import orchestrator
from rag_agent import build_vector_store


def main():
    # Load environment variables
    load_dotenv()

    # Validate API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")

    # Initialize Groq client
    client = Groq(api_key=api_key)

    # Resolve project paths
    project_dir = Path(__file__).resolve().parent
    pdf_path = project_dir.parent / "2.)rag" / "Quantum Computing.pdf"

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found at: {pdf_path}")

    # Build vector store ONCE
    print("Building vector store... (this may take a few seconds)")
    vectorstore = build_vector_store(pdf_path)
    print("Vector store ready.\n")

    # Start interaction loop
    print("AI Research Assistant Started (type 'exit' to quit)")

    while True:
        try:
            query = input("\nEnter your query:\n").strip()
        except EOFError:
            print("\nInput stream closed. Exiting.")
            break

        if query.lower() == "exit":
            print("Exiting...")
            break

        if not query:
            print("Please enter a valid query.")
            continue

        # Call orchestrator
        result = orchestrator(query, vectorstore, client)

        print("\nFinal Answer:\n")
        print(result)


if __name__ == "__main__":
    main()