from groq import Groq
from groq import BadRequestError
import os
from pathlib import Path
from dotenv import load_dotenv

script_dir = Path(__file__).resolve().parent

# Support both common local env-file names.
for env_name in (".env", "env"):
    env_path = script_dir / env_name
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        break


def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing GROQ_API_KEY. Add it to environment or create "
            f"{script_dir / '.env'} (or {script_dir / 'env'}) with: "
            "GROQ_API_KEY=your_key_here"
        )
    return Groq(api_key=api_key)


client = get_client()
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

def summarize(text, mode="short"):
    if mode == "short":
        prompt = "Summarize in 3 bullet points."
    elif mode == "detailed":
        prompt = "Summarize in detailed bullet points."
    elif mode == "technical":
        prompt = "Summarize focusing on technical insights."
    else:
        prompt = "Summarize clearly."

    full_prompt = f"{prompt}\n\n{text}"

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )
    except BadRequestError as exc:
        # Surface a clear message when a configured model is no longer available.
        if "decommissioned" in str(exc).lower():
            raise RuntimeError(
                f"Configured model '{MODEL_NAME}' is decommissioned. "
                "Set GROQ_MODEL in .env to a currently supported model."
            ) from exc
        raise

    return response.choices[0].message.content


if __name__ == "__main__":
    text = input("Enter text:\n")
    mode = input("Mode (short/detailed/technical): ")

    print("\nSummary:\n")
    print(summarize(text, mode))