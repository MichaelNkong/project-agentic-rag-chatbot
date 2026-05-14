#  Agentic RAG Chatbot (Dockerized)
# 🚀 Demo
A simple demo of the RAG Chatbot is shown below. A user can ask questions about contents in documents(Cloud computing and requirement Engineering and gets retrieved answer based on similarity search:

[demo1.mp4](..%2F..%2FDownloads%2Fdemo1.mp4)

A production-ready **Retrieval-Augmented Generation (RAG)** chatbot built with a modular backend architecture using Docker.
This project demonstrates practical skills in **LLM integration, backend engineering, agent orchestration, and containerized deployment**.

---

# 🚀 Overview

This application allows users to query a knowledge base using natural language.
It combines semantic document retrieval with LLM reasoning to generate context-aware responses.

The system uses a custom `rag_query_tool` integrated directly into the service layer for retrieval and response generation.

---

# ✨ Key Features

- 🔍 Semantic document retrieval using vector embeddings
- 🧠 LLM-powered response generation
- 🔌 Custom `rag_query_tool` for RAG workflows
- 🤖 Agent-based orchestration with CrewAI
- 🐳 Fully containerized with Docker
- 📄 Automated document ingestion pipeline
- 📈 Logging and debugging support
- ⚙️ Modular and testable backend structure

---

# 🧱 Architecture

```text
User → FastAPI Backend → Service Layer → rag_query_tool → LLM
                                                ↓
                                          Vector Store
```

# 🧩 Core Components

## FastAPI Backend

Handles incoming API requests and routes chat interactions through the service layer.

Location:

```text
src/backend/
```
## Service Layer
Contains business logic and orchestrates the chatbot workflow.

Location:

```text
src/backend/services/chat.py
```

## RAG Query Tool

Custom retrieval tool responsible for:

- Querying vector embeddings
- Retrieving relevant documents
- Building contextual prompts
- Sending prompts to the LLM
- Returning grounded responses

Location:

```text
src/tools/rag_query_tool.py
```

## Document Ingestion Pipeline

Processes and ingests documents into the vector store.

Location:

```text
src/rag_doc_ingestion/
```

Main ingestion script:

```text
src/rag_doc_ingestion/ingest_docs.py
```

## Agent Orchestration

CrewAI agents and orchestration logic.

Location:

```text
src/agent/
```
# 🛠 Tech Stack

- **Backend:** Python, FastAPI
- **LLM:** OpenAI API
- **Agent Framework:** CrewAI
- **RAG Workflow:** Custom `rag_query_tool`
- **Vector Search:** Embedding similarity search
- **Containerization:** Docker
- **Observability:** Python logging
- **Environment Management:** `.env`

---

# 🐳 Running with Docker

## 1. Build the Docker image

```bash
docker build -t rag-chatbot .
```

## 2. Create the container

```bash
docker run -d --name -e API_KEY="" rag-chatbot -p 8000:8000 rag-chatbot
```

## 3. Start the container

```bash
docker start rag-chatbot
```

---

## 4. Access the API

```text
http://localhost:8000
```

# ⚙️ Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
CREWAI_DISABLE_TELEMETRY=true
HOME=/tmp
```

# 🔌 API Example

## POST `/chat/answer`

### Request

```json
{
  "chat_history": [
    {
      "role": "user",
      "content": "What is a RESTful API?"
    }
  ]
}
```

### Response

```json
{
  "answer": "...",
  "sources": [...],
  "tool_used": "rag_query_tool"
}
```

# ⚠️ Challenges & Solutions

## 🔄 Simplifying Architecture

- **Problem:** Maintaining a separate MCP server increased deployment complexity.
- **Solution:** Moved tool execution directly into the backend service layer.

---

## ⏱ RAG Workflow Optimization

- **Problem:** Additional service communication added unnecessary latency.
- **Solution:** Direct invocation of `rag_query_tool` improved performance and maintainability.

---

## 🔐 Secret Management

- **Problem:** Risk of exposing API keys during development.
- **Solution:** Used environment variables and `.gitignore` protection.

---

## ⚙️ Docker Runtime Issues

- **Problem:** CrewAI encryption and permission issues inside containers.
- **Solution:** Configured writable `HOME` directory and disabled telemetry.

---

# 📦 Project Structure

```text
project-agentic-rag-chatbot/
│
├── doc_dir/
│
├── src/
│   ├── agent/
│   │   ├── agents/
│   │   ├── config/
│   │   ├── llm/
│   │   │   ├── llm_configuration.py
│   │   │   └── load_llm.py
│   │   ├── tasks/
│   │   ├── crew.py
│   │   └── crew_orchestration.py
│   │
│   ├── backend/
│   │   ├── api/
│   │   ├── config/
│   │   ├── services/
│   │   │   └── chat.py
│   │   └── main.py
│   │
│   ├── rag_doc_ingestion/
│   │   ├── config/
│   │   └── ingest_docs.py
│   │
│   └── tools/
│       └── rag_query_tool.py
│
├── Dockerfile
├── start.sh
├── requirements.txt
├── runtime.txt
├── .env
└── README.md
```

# 🧠 What This Project Demonstrates

- Building production-style RAG systems
- Designing modular AI backend architectures
- Agent orchestration with CrewAI
- Semantic search integration
- Containerized application deployment
- Secure configuration handling
- Backend debugging and observability

---

# 🎯 Future Improvements

- Add response caching
- Implement async task processing
- Add authentication and rate limiting
- Improve observability with metrics and tracing
- Deploy to cloud infrastructure (AWS ECS / EC2)
- Add CI/CD pipelines for automated deployment

---

# 👨‍💻 Author

Michael
Software Engineer | Test Automation | Backend & AI Systems

---

# ⭐ Why This Project Matters

This project reflects real-world engineering challenges in AI systems:

- LLM integration
- RAG workflow design
- Backend modularization
- Containerized deployment
- Performance optimization

It showcases not only coding ability, but also **software engineering and system design thinking**.