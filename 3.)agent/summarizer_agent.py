def summarizer_agent(text, client):
    prompt = f"""
Summarize the following content clearly.

If it is a question, answer it briefly instead.

Content:
{text}
"""
    prompt = f"Summarize the following text clearly:\n\n{text}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content