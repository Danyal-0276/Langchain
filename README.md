# 🦜🔗 LangChain Masterclass & Learning Lab

An end-to-end collection of hands-on Python modules, interactive Streamlit applications, and standalone labs for mastering **LangChain**, **Prompt Engineering**, **Structured Output Extraction**, and **Multi-Provider LLM Integrations** (OpenAI, Anthropic, Google Gemini, Hugging Face, and Ollama).

---

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://python.langchain.com/"><img src="https://img.shields.io/badge/LangChain-v0.3%2B-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"></a>
  <a href="https://ollama.com/"><img src="https://img.shields.io/badge/Ollama-Qwen_2.5-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"></a>
  <a href="https://docs.pydantic.dev/"><img src="https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic"></a>
</p>

<p align="center">
  <a href="https://platform.openai.com/docs"><img src="https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI"></a>
  <a href="https://docs.anthropic.com/"><img src="https://img.shields.io/badge/Anthropic-Claude_3.5-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic"></a>
  <a href="https://ai.google.dev/gemini-api/docs"><img src="https://img.shields.io/badge/Google-Gemini_1.5-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Google Gemini"></a>
  <a href="https://huggingface.co/docs"><img src="https://img.shields.io/badge/Hugging_Face-Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face"></a>
  <img src="https://img.shields.io/badge/Status-Active_Lab-2EA44F?style=flat-square" alt="Status">
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features & Architecture](#-key-features--architecture)
- [Repository Structure](#-repository-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Environment Setup](#-installation--environment-setup)
- [Module Deep-Dives & Usage](#-module-deep-dives--usage)
  - [1. Langchain Models (`/Langchain models`)](#1-langchain-models-langchain-models)
  - [2. Prompt Engineering & UI (`/Prompts`)](#2-prompt-engineering--ui-prompts)
  - [3. Structured Output & Schemas (`/Structured output`)](#3-structured-output--schemas-structured-output)
- [Running Interactive Streamlit Apps](#-running-interactive-streamlit-apps)
- [Security & Credentials](#-security--credentials)
- [License & Contributions](#-license--contributions)

---

## 💡 Overview

This repository serves as a **complete hands-on curriculum and practical sandbox** for building modern AI applications with **LangChain**. It bridges the gap between cloud-hosted foundation models (OpenAI GPT, Anthropic Claude, Google Gemini) and privacy-first local LLMs (Ollama Qwen 2.5, Hugging Face TinyLlama).

Whether you are implementing semantic document similarity search, building interactive Streamlit prompt interfaces, creating conversational CLI bots, or enforcing strict schema parsing with Pydantic and JSON Schema, this repository provides copy-pasteable, production-ready patterns.

---

## 🔥 Key Features & Architecture

| Module | Core Concepts Demonstrated | Technologies Used |
| :--- | :--- | :--- |
| **Model Integrations** | Multi-provider Chat Models, Text Generation, Local Pipelines, Document Embeddings, Cosine Similarity ranking | LangChain Core, OpenAI API, Anthropic, Google Gemini, Hugging Face Hub / Transformers, PyTorch |
| **Prompt Engineering** | `PromptTemplate`, `ChatPromptTemplate`, `MessagesPlaceholder`, Prompt Serialization (`JSON`), CLI Chatbot, Web UI | Ollama (`qwen2.5:3b`), Streamlit, `python-dotenv` |
| **Structured Output** | `.with_structured_output()`, Pydantic V2 Models, TypedDict Annotations, Raw JSON Schema validation | Pydantic, TypedDict, Ollama, TinyLlama |

---

## 📂 Repository Structure

```text
.
├── Langchain models/               # Cloud & Local Model Integrations
│   ├── ChatModels/
│   │   ├── chat_model_openai.py          # OpenAI GPT Chat Completion wrapper
│   │   ├── chatmodel_anthropic.py        # Anthropic Claude 3 wrapper
│   │   ├── chatmodel_google.py           # Google Gemini Generative AI integration
│   │   ├── chatmodel_hf_local.py         # Local Qwen Hugging Face pipeline execution
│   │   └── chatmodel_huggingface_api.py  # Hosted Hugging Face Inference API endpoint
│   ├── EmbeddedModels/
│   │   ├── doc_similarity.py             # Semantic document search using Cosine Similarity
│   │   ├── embedding_hf.py               # Local sentence-transformers embeddings (all-MiniLM-L6-v2)
│   │   ├── embedding_openai_query.py     # Single-query OpenAI vector embedding generator
│   │   └── embeddings_openai_docs.py     # Batch document vector embedding with OpenAI
│   └── LLMs/
│       └── _llm_demo.py                  # Legacy instruct/completion text model wrapper
│
├── Prompts/                        # Prompt Design, Serialization & Applications
│   ├── chat_prompt_template.py           # Domain/Topic template formatting
│   ├── chatbot.py                        # Terminal CLI Chatbot with persistent chat history
│   ├── message_placeholder.py            # Dynamic history injection via MessagesPlaceholder
│   ├── messages.py                       # System, Human, and AI message object manipulation
│   ├── prompt_gen.py                     # Programmatic template generator saving to template.json
│   ├── prompt_ui.py                      # Interactive Streamlit Web App for Research Paper summarization
│   └── template.json                     # Serialized JSON PromptTemplate
│
├── Structured output/              # Schema-Driven LLM Data Extraction
│   ├── json_schema.json                  # Reusable JSON Schema definition for product reviews
│   ├── pydantic_demo.py                  # Standalone Pydantic field validation & JSON serialization
│   ├── typedict_demo.py                  # Python TypedDict comparison matrix
│   ├── with_structered_output_llama.py   # Structured extraction with local TinyLlama pipeline
│   ├── with_structered_output_pydantic.py# Sentiment & theme extraction returning Pydantic objects
│   ├── with_structered_output_typedict.py# Structured output returning Python dictionaries
│   └── with_structured_output_json.py    # Schema enforcement via raw JSON Schema dicts
│
├── .gitignore                      # Git exclusion rules for API keys, cache, virtualenvs
├── requirements.txt                # Unified project dependencies
└── README.md                       # Comprehensive repository documentation
```

---

## ⚡ Prerequisites

- **Python**: `3.10` or higher
- **Ollama** (Optional for local execution): Installed and running locally with `qwen2.5:3b` pulled:
  ```bash
  ollama pull qwen2.5:3b
  ```
- **Hardware**: Dedicated GPU recommended for running local PyTorch / Hugging Face models (`TinyLlama-1.1B`).

---

## ⚙️ Installation & Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Danyal-0276/langchain-learning.git
cd langchain-learning
```

### 2. Set Up Virtual Environment

- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory (or inside subdirectories if running modularly) with your credentials:

```dotenv
# Cloud Provider API Keys (Optional based on which examples you run)
OPENAI_API_KEY="sk-proj-your-openai-key"
ANTHROPIC_API_KEY="sk-ant-your-anthropic-key"
GOOGLE_API_KEY="AIzaSy-your-google-api-key"
HUGGINGFACEHUB_API_TOKEN="hf_your_huggingface_token"
```

> 🔒 **Security Notice**: `.env` is ignored by `.gitignore`. Never commit API keys to public repositories.

---

## 🚀 Module Deep-Dives & Usage

### 1. Langchain Models (`/Langchain models`)

Demonstrates how LangChain provides a unified interface across cloud APIs and local inference engines.

* **Hosted Chat Models**:
  ```bash
  python "Langchain models/ChatModels/chat_model_openai.py"
  python "Langchain models/ChatModels/chatmodel_anthropic.py"
  python "Langchain models/ChatModels/chatmodel_google.py"
  ```
* **Local Hugging Face Models**:
  ```bash
  python "Langchain models/ChatModels/chatmodel_hf_local.py"
  ```
* **Semantic Document Similarity**:
  Computes high-dimensional vector embeddings and calculates cosine similarity between user queries and text corpora:
  ```bash
  python "Langchain models/EmbeddedModels/doc_similarity.py"
  ```

---

### 2. Prompt Engineering & UI (`/Prompts`)

Focuses on building structured, reusable prompts and interactive user interfaces.

* **CLI Interactive Chatbot**:
  Maintains stateful chat history in a loop using Ollama (`qwen2.5:3b`):
  ```bash
  python Prompts/chatbot.py
  ```
* **Prompt Serialization**:
  Export prompt definitions to JSON and reload them dynamically:
  ```bash
  python Prompts/prompt_gen.py
  python Prompts/message_placeholder.py
  ```

---

### 3. Structured Output & Schemas (`/Structured output`)

Learn how to enforce reliable, machine-readable responses (JSON, dictionaries, Pydantic objects) from LLMs.

* **Pydantic Model Extraction**:
  Passes a Pydantic schema to `.with_structured_output()` to extract key themes, sentiment (positive/negative/neutral), pros, cons, and reviewer names from unstructured text:
  ```bash
  python "Structured output/with_structered_output_pydantic.py"
  ```
* **TypedDict & JSON Schema Parsing**:
  ```bash
  python "Structured output/with_structered_output_typedict.py"
  python "Structured output/with_structured_output_json.py"
  ```
* **Local TinyLlama Structured Output**:
  Executes structured data extraction entirely offline using Hugging Face pipelines:
  ```bash
  python "Structured output/with_structered_output_llama.py"
  ```

---

## 🖥️ Running Interactive Streamlit Apps

Launch the Research Paper Summarizer web app built with Streamlit and LangChain:

```bash
streamlit run Prompts/prompt_ui.py
```

Features:
- Select from benchmark AI papers (*Attention Is All You Need*, *GPT-3*, *BERT*, *Diffusion Models*).
- Select target style (*Beginner-Friendly*, *Technical*, *Mathematical*, *Code-Oriented*).
- Choose output length and generate structured summaries powered by Ollama.

---

## 🔐 Security & Credentials

- Keep all secret keys inside `.env`.
- Ensure provider quotas and usage spending limits are configured in OpenAI/Anthropic dashboards.
- For local privacy-sensitive workloads, rely on the `Ollama` or `transformers` local pipelines provided in the repository.

---

## 📄 License & Contributions

Distributed under the **MIT License**. Contributions, bug reports, and pull requests are welcome!

```text
Crafted with ❤️ for the AI & Open-Source Community.
```

