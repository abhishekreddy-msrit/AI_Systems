import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

client = None


def create_groq_client():
    script_dir = Path(__file__).resolve().parent

    # Prefer .env next to this file, then fall back to current working directory.
    load_dotenv(script_dir / ".env")
    load_dotenv()

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing GROQ_API_KEY. Add it in 3.)agent/.env as GROQ_API_KEY=your_key "
            "or set it in your conda env with: conda env config vars set GROQ_API_KEY=your_key"
        )

    if api_key == "your_groq_api_key_here" or not api_key.startswith("gsk_"):
        raise ValueError(
            "Invalid GROQ_API_KEY format in 3.)agent/.env. Use your real Groq key (starts with gsk_)."
        )

    return Groq(api_key=api_key)

# -------------------------
# TOOL 1: Summarizer
# -------------------------
def summarize_tool(text):
    prompt = f"Summarize the following in 3 clear bullet points:\n\n{text}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# -------------------------
# TOOL 2: General Answer
# -------------------------
def answer_tool(query):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": query}]
    )

    return response.choices[0].message.content


# -------------------------
# PLANNER (Decision Maker)
# -------------------------
def decide_tool(user_input):
    prompt = f"""
You are an AI agent.

Decide which tool to use:
- "summarize" → if user asks to summarize text
- "answer" → for general questions or explanations

Respond ONLY with one word: summarize OR answer

User input:
{user_input}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip().lower()


# -------------------------
# MAIN LOOP
# -------------------------
def main():
    global client

    try:
        client = create_groq_client()
    except ValueError as exc:
        print(f"Setup error: {exc}")
        return

    print("AI Agent Started (type 'exit' to quit)\n")

    while True:
        user_input = input("Enter task:\n")

        if user_input.lower() == "exit":
            print("Exiting agent...")
            break

        tool = decide_tool(user_input)

        if "summarize" in tool:
            text = input("Enter text to summarize:\n")
            result = summarize_tool(text)

        elif "answer" in tool:
            result = answer_tool(user_input)

        else:
            result = "Could not decide which tool to use."

        print("\nResult:\n")
        print(result)
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()