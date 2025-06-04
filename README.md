# 🧠 Neuroscience RAG Assistant Chatbot

The Brain RAG Assistant is an **AI-powered knowledge system** that provides expert answers about the human brain. Powered by **FAISS vector search and Sentence Transformers**, it retrieves precise information from your PDF documents and delivers responses through Groq's ultra-fast LLMs (like LLaMA-3) - all within a beautiful chat Streamlit interface.

This system combines advanced retrieval technology with conversational AI to create a personalized neuroscience tutor that only answers from your trusted knowledge base.

---

## 🚀 How It Works

### 📄 Step 1: Knowledge Base Preparation  
Users add their neuroscience PDF (e.g., "brain.pdf") to the `data/` folder.

### 🔍 Step 2: Intelligent Document Processing  
The system:
- Extracts text using PyPDF2  
- Chunks content for optimal retrieval  
- Generates embeddings with Sentence Transformers  
- Builds a FAISS vector search index  

### 💬 Step 3: Natural Language Queries  
Users ask questions through a chat interface:
1. Questions are converted to embeddings  
2. FAISS finds the most relevant document passages  
3. Groq's LLM synthesizes accurate answers  

### 🧠 Step 4: Context-Aware Responses  
The system maintains conversation history and only answers from the provided PDF, ensuring reliable information.

---

## 🛠️ Tech Stack & Purpose

| Technology          | Role                                                                 |
|---------------------|----------------------------------------------------------------------|
| Streamlit           | 💅 WhatsApp-style chat interface with message history                |
| FAISS               | 🔍 Ultra-fast vector similarity search                               |
| SentenceTransformers| 🏷️ State-of-the-art text embeddings                                  |
| Groq API            | ⚡ Lightning-fast LLM responses (LLaMA-3)                            |
| PyPDF2              | 📄 Text extraction from PDF documents                                |
| Python              | 🐍 Core retrieval and generation logic                               |

---

## 🧰 Source Files

| File                  | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `app.py`              | 🚀 Main Streamlit application with chat UI                                  |
| `utils/pdf_processor.py` | 📄 PDF text extraction and chunking logic                                |
| `utils/embedding_handler.py` | 🏷️ Sentence Transformers + FAISS indexing pipeline              |
| `utils/rag_helper.py` | 🧠 Groq API integration for LLM responses                                   |
| `requirements.txt`    | 📦 Python dependencies                                                      |
| `.env`                | 🔐 Stores `GROQ_API_KEY` for secure LLM access                             |

---

## 🖼️ System Architecture
![deepseek_mermaid_20250604_9e3baa](https://github.com/user-attachments/assets/930ff051-e2b1-4925-a819-37fbe0b706dc)

---

## 📸 Screenshots
*chat interface with message history*
![Screenshot 2025-06-04 184724](https://github.com/user-attachments/assets/7613c15c-82dd-4d62-8d75-fe9f46e962e6)  

![Screenshot 2025-06-04 184742](https://github.com/user-attachments/assets/401b4172-8fb3-48e2-a81b-4fa7c90dda61)
  

![Screenshot 2025-06-04 184851](https://github.com/user-attachments/assets/537fbc1d-8b46-48f0-a0df-e43c3585fe04)
  
---

## 🔮 Future Improvements

- ✨ Support for multiple PDF knowledge sources  
- 📊 Visual knowledge graph of brain concepts  
- 🔍 Advanced semantic search with hybrid retrieval  
- 🎤 Voice input/output capabilities  
- 📱 Mobile-optimized interface  

