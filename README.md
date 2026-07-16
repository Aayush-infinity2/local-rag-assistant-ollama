# Local RAG Assistant with Ollama

> A privacy-focused Retrieval-Augmented Generation (RAG) assistant that answers questions from a custom local knowledge base using Ollama and Streamlit.

## Overview

Local RAG Assistant runs fully on your computer. It searches a local text knowledge base, finds information relevant to a question, and uses a local Ollama language model to generate a grounded answer. No cloud AI API key or paid account is required.

**GitHub description:** A privacy-focused Retrieval-Augmented Generation (RAG) assistant built with Streamlit and Ollama. It performs local semantic search over a custom knowledge base and generates grounded AI responses using local language models.

## Features

- Local AI models through Ollama
- Semantic search with embeddings and cosine similarity
- Streamlit chat interface with streamed answers
- Retrieved context and similarity-score display
- Adjustable number of context chunks
- Easy-to-edit local text knowledge base
- `uv` dependency management

## How it works

```text
User question → embedding model → relevant context chunks → local LLM → answer
```

Every non-empty line in `data/knowledge_base.txt` is a **context chunk**. The app retrieves the chunks most similar to the question and provides them to the AI model before it answers.

## Project structure

```text
ollama-rag-assistant/
├── app.py                     # Main Streamlit application
├── README.md                  # Project documentation
├── pyproject.toml             # uv configuration
├── requirements.txt           # Dependency list
├── .gitignore
├── data/
│   └── knowledge_base.txt     # Information used for answers
└── src/
    ├── config.py
    ├── ollama_service.py
    └── rag.py
```

## Requirements

- Windows 10 or Windows 11
- Internet connection for the initial setup and model downloads
- Approximately 4 GB free disk space for the default models
- Ollama
- uv

## Installation and first run

### 1. Get the project

If you received a ZIP file, right-click it, select **Extract All**, and open the extracted `ollama-rag-assistant` folder.

Or clone it from GitHub:

```powershell
git clone https://github.com/YOUR-USERNAME/local-rag-assistant-ollama.git
cd local-rag-assistant-ollama
```

### 2. Install Ollama

1. Visit [ollama.com/download](https://ollama.com/download).
2. Download and install Ollama for Windows.
3. Close PowerShell, then open a new PowerShell window.
4. Verify the installation:

```powershell
ollama --version
```

### 3. Install uv

Open PowerShell and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close PowerShell, open it again, and verify:

```powershell
uv --version
```

### 4. Download the local AI models

Run these commands once:

```powershell
ollama pull hf.co/CompendiumLabs/bge-base-en-v1.5-gguf
ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
```

The first model finds relevant information. The second model generates answers.

### 5. Open the project folder

Open the project folder in File Explorer. Click its address bar, type `powershell`, and press Enter.

Or run a command like this:

```powershell
cd "C:\Users\YourName\Documents\ollama-rag-assistant"
```

### 6. Install dependencies and start the app

Run:

```powershell
uv sync
uv run streamlit run app.py
```

Open the link shown in PowerShell, normally `http://localhost:8501`.

To stop the app, press `Ctrl + C` in PowerShell.

## How to use the app

1. Open the local URL in your browser.
2. Ask a question, for example: `How long do cats sleep?`
3. Read the generated response.
4. Expand **Retrieved context** to inspect the exact knowledge-base lines used.

The **Context chunks** slider controls how many relevant lines are given to the AI:

- **1–2:** faster, focused answers for simple questions
- **3:** recommended balanced default
- **4–5:** more context for broad questions, but possibly less focused answers

## Add your own knowledge base

Open `data/knowledge_base.txt`. Add one complete fact or short paragraph on each new line:

```text
The college library is open from 9 AM to 5 PM on weekdays.
Students can borrow up to four books at one time.
The computer laboratory is located on the second floor.
```

Save the file, stop the application, and run `uv run streamlit run app.py` again. The app will then create embeddings for and use the new information.

## Uploading to GitHub

Suggested repository name: `local-rag-assistant-ollama`

Suggested topics: `rag`, `ollama`, `streamlit`, `local-llm`, `generative-ai`, `embeddings`, `semantic-search`, `python`, `machine-learning`.

Include these files and folders in GitHub or a ZIP:

```text
app.py
README.md
pyproject.toml
requirements.txt
.gitignore
data/
src/
uv.lock (if created after uv sync)
```

Do not include `.venv/`, `__pycache__/`, or `.git/`.

## Live-link note

This is a **local-first application**. It needs Ollama and the downloaded models to run on the same computer as the app. A regular public Streamlit deployment cannot run this exact setup unless its cloud server is also configured with Ollama and the models.

For an academic submission, share the GitHub repository, this README, screenshots, and a short demo video. The local design demonstrates privacy-focused and offline-capable AI.

## Troubleshooting

| Problem | Solution |
| --- | --- |
| `uv` is not recognized | Close and reopen PowerShell. If needed, repeat the uv installation step. |
| `ollama` is not recognized | Install Ollama, then close and reopen PowerShell. |
| Ollama is unavailable in the app | Open Ollama from the Start menu, wait a few seconds, then refresh the app. |
| Model is missing | Run the two `ollama pull` commands again. |
| Port 8501 is busy | Run `uv run streamlit run app.py --server.port 8502`, then open `http://localhost:8502`. |

## Future improvements

- PDF and TXT document upload
- Minimum similarity threshold for unrelated questions
- Persistent vector database for larger knowledge bases
- Source citations with file names and line numbers
- Retrieval-quality evaluation using test questions

## Educational value

This project demonstrates local large language models, embeddings, semantic search, cosine similarity, RAG, prompt grounding, and user-interface development. It is a strong project for a 3rd-year B.Tech AI/ML/CSE student.
