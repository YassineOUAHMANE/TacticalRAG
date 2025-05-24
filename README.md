# ⚽ TacticalRAG

**TacticalRAG** is an AI-powered football analysis assistant built using **Retrieval-Augmented Generation (RAG)**. It provides real-time, context-aware responses to natural language questions using football knowledge from match reports, tactical breakdowns, player statistics, and historical data.

Whether you're a **coach**, **analyst**, **journalist**, or a **passionate fan**, TacticalRAG gives you insights grounded in actual documents—fast and intelligently.

![TacticalRAG App](./frontend/public/football_backround.jpg)

---

## 🔍 Features

- 💡 **Context-Aware Q&A** — Ask questions like "How did Manchester City press against Liverpool in 2023?" or "Compare Benzema’s role in 2018 vs 2022."
- 📚 **RAG Architecture** — Combines retrieval (FAISS/Chroma vector search) with LLM-based generation.
- ⚙️ **Modular Pipeline** — Flexible backend with document ingestion, chunking, embedding, and query processing.
- 🌍 **Multilingual Ready** — Handle queries in multiple languages with consistent context grounding.

---

## 🚀 Tech Stack

- 🧠 **LLM**: OpenAI GPT / TinyLLaMA (configurable)
- 🖙️ **Backend**: FastAPI
- 🔎 **Retrieval**: FAISS or Chroma (configurable)
- 🖼️ **Frontend**: React + TailwindCSS
- 🗃️ **Document Processing**: LangChain
- 🧠 **Embeddings**: SentenceTransformers / OpenAI Embeddings

---

## 💠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YassineOUAHMANE/tacticalrag.git
cd tacticalrag
```

### 2. Backend Setup (FastAPI)

```bash
cd backend
conda env create -f environment.yml
conda activate TacticalRAG


# Start FastAPI server
uvicorn backend.main:app --reload
```

### 3. Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

> 🌐 The app should now be running on `http://localhost:3000` (frontend) and `http://localhost:8000` (backend API).

---


## ✨ Example Queries

- *"How did Real Madrid defend against PSG in the 2022 UCL?"*
- *"Which player had the highest xG in the World Cup final?"*
- *"Describe Arsenal's 2022-23 build-up strategy under Arteta."*

---

## 🧪 Testing

You can use the `/docs` endpoint from FastAPI to test your backend directly:

```
http://localhost:8000/docs
```

---

## 🤝 Contributing

Pull requests are welcome! If you have new ideas, model integrations, or UI enhancements, feel free to contribute.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Open a pull request

---

