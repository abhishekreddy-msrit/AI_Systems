def verifier_agent(answer, context, client):
    prompt = f"""
You are a strict verifier.

Check whether the answer is fully supported by the context.

Rules:
- If the answer is fully supported → respond EXACTLY: VALID
- If the answer is not supported → respond EXACTLY: NOT_VALID

Do NOT explain.
Do NOT add anything else.

Context:
{context}

Answer:
{answer}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content.strip().lower()

    if "valid" in result and "not" not in result:
        return "VALID"
    else:
        return "NOT_VALID"