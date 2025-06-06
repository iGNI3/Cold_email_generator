
# 📧 Cold Email Generator using Llama 3.1 and LangChain

This project is an end-to-end Generative AI application that automates cold outreach for business development teams. By scraping job descriptions from career pages, intelligently extracting structured job info, and mapping it to a company’s portfolio, the system generates tailored cold emails—powered by Llama 3.3 and LangChain.

---

## Features

- ✅ Web scraping of job postings
- ✅ Extraction of role, experience, skills, and descriptions using LLM
- ✅ Intelligent portfolio link matching using ChromaDB
- ✅ Personalized cold email generation
- ✅ Intuitive Streamlit UI for interaction
- ✅ Modular and production-friendly codebase

---

## Tech Stack

| Component       | Tech Used                       |
|----------------|----------------------------------|
| LLM             | Llama 3.3 (via Groq API)         |
| App Framework   | Streamlit                        |
| Orchestration   | LangChain                        |
| Vector DB       | ChromaDB                         |
| Data Handling   | Pandas, uuid                     |
| Utils           | Regex-based text cleaning        |

---

## Screenshot
![alt text](image.png) 
![alt text](image-1.png)
![alt text](image-2.png)

---

##  Getting Started

### 1. Clone the repository

```
use groq cloud for the api

```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Prepare your portfolio CSV

Place `my_portfolio.csv` in the path:


The CSV should have two columns:
- `Techstack` — comma-separated keywords/skills
- `Links` — URLs to your past projects

### 5. Run the app

```bash
streamlit run main.py
```

---

## Project Structure

```
├── main.py            # Streamlit app interface
├── chains.py          # LLM chains for extraction and generation
├── portfolio.py       # Portfolio ingestion & query
├── utils.py           # Text preprocessing
├── .env               # API key for Groq
└── my_portfolio.csv   # Portfolio database (not shared)
```

---

## Use Case

This tool is ideal for:
- Business development executives
- Freelancers or consultancies
- AI-based outreach optimization
- Personalized lead generation from scraped content

---

## Example Job URL

Use a job URL like:

```
https://careers.nike.com/data-engineer-itc/job/R-63119
```

---

## Deployment (Optional)

You can deploy this to:
- **Streamlit Cloud**
- **Hugging Face Spaces** (with minor tweaks)
- **Docker + FastAPI** (future enhancement)

---



