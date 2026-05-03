# 🤖 AI Sales Co-Pilot

An end-to-end AI system that analyzes, scores, and responds to inbound leads using LLMs, vector search (RAG), and a modular multi-agent architecture.

---

## 🚀 Overview

This project simulates a real-world AI sales assistant that can:

- Understand user intent from incoming leads  
- Classify and prioritize leads (HOT / WARM / COLD)  
- Generate context-aware responses using company knowledge  
- Recommend next actions automatically  

---

## 🧠 Key Features

### 🔍 Lead Analysis
Extracts:
- Intent (pricing, demo, support, etc.)
- Urgency (low, medium, high)
- Sentiment (positive, neutral, negative)

---

### 📊 Lead Scoring System
Applies rule-based logic to classify leads:
- 🔥 HOT → High priority  
- ⚠️ WARM → Follow-up needed  
- ❄️ COLD → Nurture  

---

### 📚 RAG (Retrieval-Augmented Generation)
- Uses FAISS vector database  
- Converts company knowledge into embeddings  
- Retrieves relevant context for accurate AI responses  

---

### 🤖 Multi-Agent Architecture

## 🏗️ System Architecture

```
User Input
   ↓
Analyzer Agent (Intent, Urgency, Sentiment)
   ↓
Scoring Agent (HOT / WARM / COLD)
   ↓
Retriever (FAISS Vector Search)
   ↓
LLM (RAG-based Response Generation)
   ↓
Action Agent (Next Step Recommendation)
   ↓
Streamlit UI (User Interface)
```

---

### ⚡ Performance Optimization
- Persistent FAISS vector storage  
- Avoids recomputing embeddings on every run  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- OpenAI API  
- FAISS (Vector Database)  
- Streamlit  

---

## 📁 Project Structure

pr-11/
│── app.py
│── backend/
│ ├── analyzer.py
│ ├── scorer.py
│ ├── rag.py
│ ├── orchestrator.py
│ ├── llm.py
│── data/
│ ├── company.txt
│── requirements.txt
│── .gitignore


---

## ⚙️ Setup & Installation

1. Clone the repository
```bash
git clone https://github.com/salamsofi/ai-sales-copilot.git
cd ai-sales-copilot


2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables
Create a .env file:
OPENAI_API_KEY=your_api_key_here

5. Run the app
streamlit run app.py


🧪 Example Use Case
Input:
Hi, I need pricing urgently


Output:
- Intent → pricing
- Urgency → high
- Score → 🔥 HOT
- AI Response → pricing details
- Action → Schedule call


🎯 Use Cases
- Lead qualification automation
- AI sales assistants
- Customer support systems
- CRM augmentation


📌 Future Improvements
- Feedback loop for smarter scoring
- Integration with CRM tools
- Email / WhatsApp automation
- API-based deployment


🔐 Security Note
- API keys are stored in .env (not committed)
- .gitignore prevents sensitive data exposure


⭐ Why this project matters
This project demonstrates:
- LLM integration with real workflows
- RAG-based context-aware generation
- Multi-agent system design
- Production-level considerations (performance + structure)


👨‍💻 Author
Mohd. Salam Sofi