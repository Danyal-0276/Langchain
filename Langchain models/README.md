# 🤖 LangChain Model Integrations Lab

This directory contains standalone examples demonstrating how to connect **LangChain** with various cloud LLM providers and local inference engines.

---

## 📌 Included Modules

### 1. Chat Models (`/ChatModels`)
- `chat_model_openai.py` — OpenAI GPT Chat Completion (`ChatOpenAI`)
- `chatmodel_anthropic.py` — Anthropic Claude 3 (`ChatAnthropic`)
- `chatmodel_google.py` — Google Gemini Generative AI (`ChatGoogleGenerativeAI`)
- `chatmodel_hf_local.py` — Local Hugging Face pipeline execution with PyTorch (`HuggingFacePipeline`)
- `chatmodel_huggingface_api.py` — Cloud Hugging Face Inference API (`HuggingFaceEndpoint`)

### 2. Embedded Models & Semantic Search (`/EmbeddedModels`)
- `embedding_openai_query.py` — Single query vector embeddings using OpenAI (`OpenAIEmbeddings`)
- `embeddings_openai_docs.py` — Document batch vector embeddings using OpenAI
- `embedding_hf.py` — Local sentence embedding generation with Hugging Face (`all-MiniLM-L6-v2`)
- `doc_similarity.py` — Complete semantic document similarity search using Cosine Similarity ranking

### 3. Text Completion Models (`/LLMs`)
- `_llm_demo.py` — Legacy instruct text completion models using OpenAI `LLM` wrappers

---

## 🚀 Execution Guide

Make sure your virtual environment is active and required provider API keys are present in your root `.env` file.

```bash
# Run OpenAI Chat Example
python "Langchain models/ChatModels/chat_model_openai.py"

# Run Google Gemini Chat Example
python "Langchain models/ChatModels/chatmodel_google.py"

# Run Semantic Document Similarity Search
python "Langchain models/EmbeddedModels/doc_similarity.py"
```

For full project documentation, return to the [Root README.md](../../README.md).

