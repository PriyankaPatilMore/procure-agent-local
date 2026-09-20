# Local ProcureAI Agent

A lightweight, local-first AI agent designed to help procurement teams analyze supplier contracts and check ERP data. 

Built to run locally without external LLM APIs (saving costs and ensuring data privacy), while still utilizing LangSmith for production-grade observability and agent tracing.

## Tech Stack
* LLM: Llama 3.2 (via Ollama)
* Embeddings: nomic-embed-text
* Agent Framework: LangGraph (ReAct architecture)
* Vector DB: Chroma (local)
* Structured Data: SQLite
* Observability: LangSmith

## Setup Instructions

1. Install Ollama on your machine.
2. Pull the necessary models:
```bash
ollama run llama3.2
ollama pull nomic-embed-text
```

3. Install Python requirements:
```bash
pip install -r requirements.txt
```

4. Setup Observability (Optional but recommended):
Copy `.env.example` to `.env` and add your LangSmith API key. This allows you to trace how the LangGraph agent routes decisions.

5. Setup the local mock database:
```bash
python setup_db.py
```

6. Run the agent:
```bash
python main.py
```

## Architecture Notes
The application uses LangGraph to route queries. If a user asks for contract details, the agent uses the RAG tool to search ChromaDB. If the user asks for financial or risk metrics, the agent queries the SQLite database directly. LangSmith is integrated to track latency, token usage, and tool routing logic.
