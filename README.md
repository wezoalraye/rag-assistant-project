# 🤖 ML Document Assistant

A RAG-powered assistant that answers Machine Learning questions from real textbooks.

## 🏗️ Architecture
User → Streamlit Frontend → FastAPI Backend → ChromaDB → Ollama LLM → Answer

## 🛠️ Tech Stack
- Python 3.10+
- FastAPI
- ChromaDB
- Sentence Transformers
- Ollama (llama3.2)
- Streamlit

## 📁 Project Structure
rag-assistant-project/
├── notebooks/ # RAG pipeline notebook
├── backend/ # FastAPI backend
├── frontend/ # Streamlit frontend
└── data/ # Vector store & raw docs


## 🚀 Setup

### 1. Clone the repo
```bash
git clone https://github.com/wezoalraye/rag-assistant-project.git
cd rag-assistant-project
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 3. Install Ollama & pull model
```bash
ollama pull llama3.2
```

### 4. Run Backend
```bash
cd backend
uvicorn app.main:app --reload
```

### 5. Run Frontend
```bash
cd frontend
streamlit run app.py
```

## ⚙️ Environment Variables
| Variable | Default | Description |
|----------|---------|-------------|
| OLLAMA_MODEL | llama3.2 | LLM model name |
| COLLECTION_NAME | ml_documents | ChromaDB collection |
| VECTOR_STORE_PATH | data/vector_store | Path to vector store |
| EMBEDDING_MODEL | all-MiniLM-L6-v2 | Embedding model |

## 📊 Evaluation Results
- Tested on 10 ML questions
- All answers grounded in source documents
- Sources cited in every response

## 📚 Data Sources
- Bishop - Pattern Recognition and Machine Learning
- Introduction to Machine Learning with Python
- Understanding Machine Learning: Theory and Algorithms