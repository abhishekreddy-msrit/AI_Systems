from rag_agent import rag_agent
from summarizer_agent import summarizer_agent
from explainer_agent import explainer_agent
from verififer_agent import verifier_agent


# LLM-Based Intent Planner-TASK Specific Prompting

def decide_intent_llm(query, client):
    prompt = f"""
You are an AI planner.

Classify the user query into ONE of the following intents:
- summarize
- explain
- research

Rules:
- "summarize" → if the user wants a shorter version
- "explain" → if the user wants understanding or simplification
- "research" → if the user is asking factual or knowledge-based questions

Respond with ONLY one word: summarize OR explain OR research

User Query:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    intent = response.choices[0].message.content.strip().lower()
    return intent


#The Orchestrator

def orchestrator(query, vectorstore, client):
    print("Deciding intent using LLM...")

    intent = decide_intent_llm(query, client)
    print(f"Detected intent: {intent}")

    
    # SUMMARIZATION FLOW
    
    if intent == "summarize":
        print("Running Summarizer Agent...")
        return summarizer_agent(query, client)

    
    # EXPLANATION FLOW
    
    elif intent == "explain":
        print("Running Explainer Agent...")
        return explainer_agent(query, client)

    
    # RESEARCH FLOW (POWERED BY RAG + VERIFICATION AT THE END)
    
    elif intent == "research":
        print("Running RAG Agent...")
        context = rag_agent(query, vectorstore)

        if not context:
            return "No relevant information found."

        print("Running Summarizer Agent...")
        summary = summarizer_agent(context, client)

        print("Running Explainer Agent...")
        explanation = explainer_agent(summary, client)

        print("Running Verifier Agent...")
        verification = verifier_agent(explanation, context, client)

        if verification == "NOT_VALID":
            return "Warning: Answer may not be fully grounded.\n\n" + explanation

        return explanation

    
    # FALLBACK
    
    else:
        return "Could not determine intent."