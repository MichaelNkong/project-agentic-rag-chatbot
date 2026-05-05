# 🤖 Agentic RAG Chatbot (Dockerized)

A production-ready **Retrieval-Augmented Generation (RAG)** chatbot built with a modular, service-oriented architecture using Docker.
This project demonstrates end-to-end skills in **LLM integration, backend engineering, testability, and system design**.

---

## 🚀 Overview

This application allows users to query a knowledge base using natural language.
It combines semantic search with LLM reasoning to provide accurate, context-aware responses.

### ✨ Key Features

* 🔍 Semantic document retrieval (vector search)
* 🧠 LLM-powered answer generation
* ⚙️ Modular microservice architecture (API + MCP service)
* 🐳 Fully containerized with Docker
* 🔌 Extensible tool-based design (agentic workflow)
* 📈 Logging and observability for debugging

---

## 🧱 Architecture

```
User → FastAPI Backend → RAG Pipeline → MCP Service → LLM
                                 ↓
                           Vector Store
```

### Components:

* **API Service (FastAPI)**
  Handles user requests and orchestrates the RAG pipeline

* **MCP Service**
  Responsible for processing knowledge queries and integrating with tools

* **Vector Store**
  Stores embeddings for semantic search

* **LLM Integration**
  Generates final responses based on retrieved context

---

## 🛠 Tech Stack

* **Backend:** Python, FastAPI
* **RAG Pipeline:** Custom implementation (retrieval + ranking)
* **LLM:** OpenAI API
* **Vector Search:** Embedding-based similarity search
* **Orchestration:** Docker, Docker Compose
* **Tooling:** CrewAI (agent-based workflow)
* **Testing & QA mindset:** Designed with testability and modularity in mind

---

## 🐳 Running with Docker

### 1. Build the image

```bash
docker build -t rag-chatbot .
```

### 2. Run with Docker Compose

```bash
docker-compose up -d
```

### 3. Access the API

```
http://localhost:8000
```

---

## ⚙️ Environment Variables

Create a `.env` file or set variables manually:

```
OPENAI_API_KEY=your_api_key
CREWAI_DISABLE_TELEMETRY=true
HOME=/tmp
```

---

## 🔌 API Example

**POST /chat/answer**

Request:

```json
{
  "chat_history": [
    {"role": "user", "content": "What is a RESTful API?"}
  ]
}
```

Response:

```json
{
  "answer": "...",
  "sources": [...],
  "tool_used": "rag_query_tool"
}
```

---

## ⚠️ Challenges & Solutions

### 🧩 Service Communication (Docker Networking)

* **Problem:** `localhost` not working between containers
* **Solution:** Used Docker service names (e.g. `mcp:5001`)

### ⏱ Timeout Issues in RAG Pipeline

* **Problem:** MCP service timing out
* **Solution:** Increased HTTP timeout and optimized request handling

### 🔐 Secret Management

* **Problem:** API key exposure blocked by GitHub
* **Solution:** Removed secrets from history and used environment variables

### ⚙️ CrewAI Initialization in Containers

* **Problem:** Encryption key error
* **Solution:** Set writable `HOME` directory and disabled telemetry

---

## 📦 Project Structure

```
.
├── src/
│   ├── api/
│   ├── mcp_server/
│   └── tools/
├── doc_dir/
├── vector_store/
├── Dockerfile
├── docker-compose.yml
└── start.sh
```

---

## 🧠 What This Project Demonstrates

* Designing scalable RAG systems
* Debugging distributed services (timeouts, networking)
* Containerization and environment isolation
* Secure handling of secrets and API keys
* Applying QA thinking to backend systems

---

## 🎯 Future Improvements

* Add caching layer for faster responses
* Introduce async processing for MCP service
* Deploy to cloud (AWS EC2 / ECS)
* Add authentication & rate limiting
* Improve observability (metrics, tracing)

---

## 👨‍💻 Author

Michael
Software Engineer | Test Automation | Backend & AI Systems

---

## ⭐ Why this project matters

This project reflects real-world challenges:

* Distributed system debugging
* LLM integration under constraints
* Production-like environment setup

It showcases not just coding ability, but **engineering thinking**.

---
