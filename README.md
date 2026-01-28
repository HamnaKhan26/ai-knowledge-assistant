# 🧠 AI Knowledge Assistant (RAG-Powered Backend)

A backend-only **AI Knowledge Assistant** built using **FastAPI**, **LangChain**, and **ChromaDB** that answers user questions using **Retrieval-Augmented Generation (RAG)** with **semantic search** and **few-shot prompting**.

This project demonstrates how to build a **production-ready AI backend** that combines embeddings, vector search, and LLMs to generate structured, context-aware responses.

---

## 🚀 Features

- **Semantic Search with Embeddings**
  - Converts documents into vector embeddings using `sentence-transformers`
  - Stores and retrieves vectors using **ChromaDB**

- **Retrieval-Augmented Generation (RAG)**
  - Retrieves relevant documents before generating answers
  - Reduces hallucinations by grounding responses in real data

- **Few-Shot Prompting**
  - Enforces structured JSON output using example-based prompting
  - Improves consistency and reliability of responses

- **FastAPI Backend**
  - Clean REST API for querying the assistant
  - Easily extendable for frontend or integrations

- **Local LLM (Free)**
  - Uses **Ollama (Mistral)** for local inference

---

## 🏗️ Tech Stack

| Layer | Technology |
|-----|-----------|
| API | FastAPI |
| LLM | Ollama (Mistral) |
| RAG Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | sentence-transformers |
| Language | Python |

---

## ✅ Prerequisites

- Python 3.10 – 3.12 installed
- Git
- Ollama installed

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/<your-username>/ai-knowledge-assistant.git
cd ai-knowledge-assistant

## Create Virtual Environment

Run this command in the project root directory:

```bash
python -m venv venv

## Activate Virtual Environment

## Windows (CMD / PowerShell)
```bash
venv\Scripts\activate

## Install Dependencies
```bash
pip install fastapi uvicorn "langchain<0.1.80" langchain-community chromadb sentence-transformers

## Install & Run Ollama
```bash
ollama run mistral

## Run the Backend Server
```bash
python -m uvicorn backend.app:app --reload

The server will start at http://127.0.0.1:8000



