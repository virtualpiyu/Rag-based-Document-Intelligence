# 🚀 SecureRAG - AI-Powered Document Intelligence Assistant

## 📌 Overview

SecureRAG is a Retrieval-Augmented Generation (RAG) application that enables intelligent question-answering from PDF documents. The system combines document processing, semantic search, vector embeddings, and Large Language Models (LLMs) to provide accurate, context-aware responses based on uploaded documents.

Instead of relying solely on a model's pre-trained knowledge, SecureRAG retrieves relevant information directly from user-provided documents, ensuring more reliable and document-specific answers.

---

## ✨ Features

* 📄 Upload and process PDF documents
* ✂️ Intelligent document chunking
* 🔍 Semantic similarity search using FAISS
* 🧠 Context-aware question answering
* 🤖 Google Gemini, OpenAi and Huggingface integration
* ⚡ Fast document retrieval and response generation
* 📚 Vector database storage for efficient search
* 🔒 Secure document-based querying

---

## 🏗️ System Architecture

```text
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Gemini LLM
      │
      ▼
Generated Response
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Frameworks & Libraries

* LangChain
* Google Gemini API
* FAISS
* PyPDF
* NumPy

### AI Technologies

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Large Language Models (LLMs)

---

## 📂 Project Structure

```text
Rag-based-Document-Intelligence/
│
├── app.py
├── Document_Loader.py
├── embedding.py
├── text_chunker.py
├── vector_db.py
├── rag_pipeline.py
├── gemini_api.py
├── requirements.txt
├── .gitignore
│
└── vectorstore/
    └── faiss_index/
        ├── index.faiss
        └── index.pkl
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/virtualpiyu/Rag-based-Document-Intelligence.git
cd Rag-based-Document-Intelligence
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file and add your Gemini API Key:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 🔍 How It Works

1. User uploads PDF documents.
2. Documents are loaded and processed.
3. Text is divided into smaller chunks.
4. Embeddings are generated for each chunk.
5. FAISS stores embeddings in a vector database.
6. User submits a question.
7. Relevant chunks are retrieved through semantic search.
8. Gemini generates an answer using retrieved context.
9. Response is displayed to the user.

---

## 🎯 Use Cases

* Research Assistance
* Academic Document Analysis
* Knowledge Base Search
* Enterprise Document Intelligence
* Internal Documentation Querying
* AI-Powered PDF Chat

---

## 📈 Future Enhancements

* Multi-document support
* Web interface improvements
* Source citation generation
* User authentication
* Cloud deployment
* Multi-language document support
* Conversation memory

---

## 👨‍💻 Author

**Piyush Kadam**

Aspiring AI & Data Science Professional | Python Developer | Generative AI Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
