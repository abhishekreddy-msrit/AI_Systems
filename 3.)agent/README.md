AI Agent System

Project Overview
This project is the third stage in the AI_Systems learning path.
The repository is organized as a step-by-step progression:
1. LLM basics
2. RAG systems
3. Agent-based systems

This module focuses on a basic tool-using AI agent built with Python and the Groq API.
It is designed to show how an LLM can route user requests to different tools in a terminal workflow.

Features
1. Task classification using an LLM
2. Tool selection based on user intent
3. Terminal-based interaction loop
4. Modular design with separate planner and tools

How It Works
Flow: User input -> LLM decision -> Tool execution -> Output

The planner function decides whether the request is a summarization task or a general question.
If the request is for summarization, the summarizer tool is used.
If the request is a general question, the answer tool is used.
The selected tool returns the final response in the terminal.

Setup Instructions
1. Clone the repository.
   git clone <repo-url>

2. Move into this module.
   cd AI_Systems/3.)agent

3. Install dependencies.
   pip install groq python-dotenv

4. Create a .env file in this folder.

5. Add your Groq key in .env.
   GROQ_API_KEY=your_api_key_here

6. Run the agent.
   python agent.py

Usage
Start the program and enter a task in the terminal.

Example inputs:
1. summarize this text
2. explain quantum computing

For summarization, the agent will ask for the text to summarize.
For general questions, it will answer directly.

Project Structure
This module lives at:
AI_Systems/3.)agent/

Main files:
1. agent.py
2. .env
3. README.md

Current Limitations
1. No multi-step reasoning
2. No memory across interactions
3. Limited tool set

Future Improvements
1. Multi-step planning with ReAct style execution
2. Tool chaining for complex tasks
3. Memory integration for context persistence
4. RAG integration for document-grounded responses

Learning Outcome
This module helps clarify:
1. The difference between a simple script and an agent
2. How tool-based execution works in practice
3. How LLM decision-making can drive task routing
