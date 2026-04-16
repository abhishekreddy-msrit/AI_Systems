Title: LLM Text Summarizer

Overview:
LLM Text Summarizer is a small Python project that takes user text and returns a summary based on the mode selected by the user. I built it as part of my AI Systems learning journey to practice prompt design, API integration, and clean workflow design for an LLM-based tool. It is useful for quickly turning long text into short, focused output depending on the use case.

Features:
1. Multiple summarization modes: short, detailed, technical
2. Prompt-controlled outputs
3. API-based LLM integration

System Architecture:
Input -> Prompt Selection -> LLM API -> Output

The script accepts user text and a selected mode. Based on the mode, it builds a different prompt. That prompt is sent to the Groq API using a selected LLaMA model, and the model response is returned as the final summary.

Tech Stack:
1. Python
2. Groq API (LLaMA 3)
3. dotenv

How It Works:
1. The script loads environment variables from a local env file.
2. It reads GROQ_API_KEY and initializes the Groq client.
3. It asks the user to enter text.
4. It asks the user to choose a mode: short, detailed, or technical.
5. It creates a prompt template based on the selected mode.
6. It sends the prompt and text to the LLM API.
7. It prints the generated summary.

Example Usage:
Run the script from the project folder:
python llm_summarizer.py

Then interact in the terminal:
Enter text:
Artificial intelligence is changing how software systems are designed and built.
Mode (short/detailed/technical): technical

Summary:
The script returns a technical-style summary focused on key engineering points.

Limitations:
1. No external knowledge retrieval is used, so there is no RAG.
2. Output quality depends heavily on prompt quality.
3. It requires a working API key and internet connection.

Scope for Future Improvements:
1. Add a RAG pipeline for grounded summaries.
2. Add a simple UI for easier interaction.
3. Add memory for better multi-step or contextual summarization.
