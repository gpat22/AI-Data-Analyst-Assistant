# 🤖 AI Data Analyst Assistant

An AI-powered data analysis system that allows users to upload datasets and query insights using natural language.

---

## 🚀 Features

- Upload CSV datasets via API
- Perform data analysis using natural language queries
- Supports operations:
  - Average
  - Maximum
  - Minimum
  - Sum
  - Count
- Dynamic column detection
- Synonym handling (e.g., salary = income, pay)
- Integrated Hugging Face model for query understanding
- Fallback rule-based system for reliability

---

## 🧠 Tech Stack

- Python
- FastAPI
- Pandas
- Hugging Face Transformers
- REST APIs

---

## 🏗️ Architecture

User Query → FastAPI → NLP (Hugging Face + Rule-based) → Pandas → Response

---

## ⚙️ How to Run

1. Clone repo
2. Install dependencies:

```bash
pip install fastapi uvicorn pandas requests
