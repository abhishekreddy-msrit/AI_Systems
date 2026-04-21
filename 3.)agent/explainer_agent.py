def explainer_agent(text, client):
    prompt = f"""
Explain the following clearly in simple terms.
Focus on understanding, not repetition.

Content:
{text}
"""
    prompt = f"Explain this in simple and clear terms:\n\n{text}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content