# LangChain Learning Lab

A collection of small, focused Python examples for learning how LangChain connects to hosted and local language models. The repository demonstrates chat models, text-completion models, embeddings, and a simple semantic-similarity workflow using OpenAI, Anthropic, Google Gemini, and Hugging Face.

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://python.langchain.com/"><img src="https://img.shields.io/badge/LangChain-Learning_Lab-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain Learning Lab"></a>
  <a href="https://platform.openai.com/docs"><img src="https://img.shields.io/badge/OpenAI-Models-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI models"></a>
  <a href="https://docs.anthropic.com/"><img src="https://img.shields.io/badge/Anthropic-Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Anthropic Claude"></a>
</p>

<p align="center">
  <a href="https://ai.google.dev/gemini-api/docs"><img src="https://img.shields.io/badge/Google-Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Google Gemini"></a>
  <a href="https://huggingface.co/docs"><img src="https://img.shields.io/badge/Hugging_Face-Models-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face models"></a>
  <img src="https://img.shields.io/badge/Status-Educational_Project-F2C94C?style=flat-square" alt="Educational project">
  <a href="https://github.com/Danyal-0276/langchain-learning/commits/main"><img src="https://img.shields.io/github/last-commit/Danyal-0276/langchain-learning?style=flat-square" alt="Last commit"></a>
  <a href="https://github.com/Danyal-0276/langchain-learning"><img src="https://img.shields.io/github/repo-size/Danyal-0276/langchain-learning?style=flat-square" alt="Repository size"></a>
</p>

> This is an educational sandbox: each script is standalone, prints its result to the terminal, and is intended to be read and run independently.

## What this project demonstrates

- Calling chat models from OpenAI, Anthropic, Google Gemini, and Hugging Face
- Running a small Hugging Face chat model locally
- Calling a hosted Hugging Face model through an inference endpoint
- Creating query and document embeddings with OpenAI and Hugging Face
- Ranking documents against a query with cosine similarity
- Loading provider credentials from a local `.env` file

## Project structure

```text
.
|-- ChatModels/
|   |-- chat_model_openai.py          # OpenAI chat example
|   |-- chatmodel_anthropic.py        # Anthropic Claude chat example
|   |-- chatmodel_google.py           # Google Gemini chat example
|   |-- chatmodel_hf_local.py         # Local Hugging Face pipeline
|   `-- chatmodel_huggingface_api.py  # Hosted Hugging Face endpoint
|-- EmbeddedModels/
|   |-- doc_similarity.py             # Semantic search with cosine similarity
|   |-- embedding_hf.py               # Hugging Face document embeddings
|   |-- embedding_openai_query.py     # OpenAI query embedding
|   `-- embeddings_openai_docs.py     # OpenAI document embeddings
|-- LLMs/
|   `-- _llm_demo.py                  # OpenAI text-completion example
|-- requirements.txt
`-- test.py                           # Prints the installed LangChain version
```

## Requirements

- Python 3.10 or newer
- Internet access for hosted model examples
- API credentials for the providers you want to use
- Enough memory and disk space to download local Hugging Face models

## Setup

1. Clone the repository and enter it:

   ```bash
   git clone https://github.com/Danyal-0276/langchain-learning.git
   cd langchain-learning
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the shared dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Install the optional packages required by specific examples:

   ```bash
   pip install langchain-anthropic sentence-transformers
   ```

   `langchain-anthropic` is required by the Anthropic example. `sentence-transformers` is required by the local Hugging Face embedding examples.

5. Create a `.env` file in the repository root and add only the credentials you need:

   ```dotenv
   OPENAI_API_KEY=your_openai_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   GOOGLE_API_KEY=your_google_api_key
   HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token
   ```

   The `.env` file is ignored by Git. Never commit real API keys.

## Running the examples

Run a script from the repository root. For example:

```bash
python ChatModels/chat_model_openai.py
python ChatModels/chatmodel_google.py
python ChatModels/chatmodel_hf_local.py
python EmbeddedModels/doc_similarity.py
```

To confirm which LangChain version is installed:

```bash
python test.py
```

## Example guide

### Chat models

- `chat_model_openai.py` sends a short prompt to an OpenAI chat model.
- `chatmodel_anthropic.py` invokes an Anthropic Claude model.
- `chatmodel_google.py` invokes a Google Gemini model.
- `chatmodel_huggingface_api.py` wraps a hosted Hugging Face endpoint as a chat model.
- `chatmodel_hf_local.py` downloads and runs a small Qwen model locally.

### Embeddings and similarity

- `embedding_openai_query.py` creates one 36-dimensional OpenAI query embedding.
- `embeddings_openai_docs.py` embeds a list of documents with OpenAI.
- `embedding_hf.py` embeds multiple sentences with `all-MiniLM-L6-v2`.
- `doc_similarity.py` embeds a query and document collection, computes cosine-similarity scores, and prints the closest document.

### Text completion

- `_llm_demo.py` is a basic OpenAI text-completion example using an instruct model.

## Notes and limitations

- Model availability and provider model IDs can change. If an example reports that a model is unavailable, replace the model name with one enabled for your account.
- Hosted examples can incur provider charges.
- The first local Hugging Face run downloads model files and can take longer than later runs.
- These scripts are learning examples, not a production application. They currently have no automated test suite, command-line interface, or shared configuration layer.
- `requirements.txt` is not version-pinned, so installs may change as upstream packages release new versions.

## Security

Keep credentials in `.env`, review provider usage limits, and avoid sending sensitive data to hosted models. If a credential is accidentally committed, revoke it immediately and remove it from the repository history.

## License

No license file is currently included. Unless a license is added, the repository's code remains under the default copyright restrictions.
