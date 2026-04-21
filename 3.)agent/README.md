AI Agent System

Project Overview
This project represents the third stage in the AI_Systems learning path.

The repository follows a structured progression:
1. LLM basics
2. RAG systems
3. Agent-based systems

This module begins with a basic tool-using agent and evolves toward a multi-agent orchestration system.

The goal is not just to build an agent, but to understand how AI systems transition from simple decision-making scripts to modular, scalable workflows.



Basic Agent (Current Implementation)

The current system is implemented in basic_agent.py.

It is a simple LLM-driven agent that:
- Takes user input from the terminal
- Uses an LLM to classify the task
- Selects the appropriate tool
- Executes the tool and returns the output

Flow:
User input -> LLM decision -> Tool execution -> Output

Tools implemented:
1. Summarizer tool
   - Summarizes input text into structured output

2. Answer tool
   - Handles general queries using the LLM

The planner (decision function) determines whether the input is:
- a summarization task
- or a general question

This forms the foundation of tool-based AI systems.



Why This Approach Matters

This basic agent demonstrates:
- how LLMs can act as decision-makers
- how tools can be modularized
- how input routing works in practice

However, while functional, this design exposes important limitations.


Limitations of the Basic Agent

1. No multi-step reasoning  
   The agent can only perform one action at a time

2. No workflow understanding  
   It cannot break down complex tasks into steps

3. Tight coupling  
   Decision-making and execution are too closely linked

4. Poor scalability  
   Adding more tools makes the system harder to manage

5. No validation  
   Outputs are not checked or verified



Transition to Multi-Agent System

To overcome these limitations, this module is being extended into a multi-agent orchestration system.

Instead of a single agent handling everything, responsibilities are divided across specialized agents.

Planned architecture:

1. Orchestrator Agent
   - Receives user input
   - Decides which agents to activate
   - Manages the workflow
   - Combines outputs

2. RAG Agent
   - Retrieves document-based context
   - Ensures grounded responses

3. Summarizer Agent
   - Processes long outputs into concise summaries

4. Analysis Agent
   - Adds reasoning, comparisons, and insights

5. Verifier Agent
   - Ensures outputs remain grounded and consistent

Flow (target system):
User input -> Orchestrator -> Specialized agents -> Final response


Setup Instructions

1. Clone the repository  
   git clone <repo-url>

2. Navigate to this module  
   cd AI_Systems/3.)agent

3. Install dependencies  
   pip install groq python-dotenv

4. Create a .env file  

5. Add your API key  
   GROQ_API_KEY=your_api_key_here

6. Run the current agent  
   python basic_agent.py


Usage

Start the program and enter a task.

Example inputs:
- summarize this text
- explain quantum computing

The agent will:
- classify the request
- choose the tool
- return the result


Project Structure

AI_Systems/3.)agent/

- basic_agent.py        current implementation
- orchestrator.py       (planned)
- rag_agent.py          (planned)
- summarizer_agent.py   (planned)
- README.md


Future Direction

This module is actively evolving toward:

- multi-agent orchestration
- tool chaining across agents
- workflow-based execution
- memory integration
- grounded reasoning using retrieval systems



Learning Outcome

This project clarifies:

1. The difference between scripts and agents  
2. How LLMs can act as decision layers  
3. Why single-agent systems fail for complex workflows  
4. How modular design leads to scalable AI systems  
5. The need for orchestration in real-world AI applications