# 🚀 AceAgents – Multi-Agent AI Recruitment Assistant

> **Hire smarter, faster, and more objectively with AI-powered recruitment.**

AceAgents is a **Multi-Agent Recruitment Intelligence System** that automates candidate screening using AI agents, RAG (Retrieval-Augmented Generation), semantic search, and live market insights.

Instead of manually reviewing hundreds of resumes, recruiters simply provide a Job Description, and AceAgents performs intelligent candidate retrieval, evaluation, ranking, comparison, and hiring recommendations.


## 🎥 Project Demo

📹 **Demo Video (Google Drive):**
[https://drive.google.com/file/d/XXXXXXXXXXXXXXXX/view?usp=sharing)](https://drive.google.com/file/d/1tfMIclEuXLGseUllI_fjpx956PJvwtT1/view?usp=sharing)



---

# ✨ Features

## 📄 AI Job Description Parser

* Extracts:

  * Required Skills
  * Preferred Skills
  * Experience
  * Education
  * Role
* Converts unstructured JDs into structured hiring requirements.

---

## 📚 Resume Knowledge Base (RAG)

* Parses resumes into structured candidate profiles
* Creates vector embeddings
* Stores embeddings in ChromaDB
* Performs semantic candidate retrieval

Instead of keyword matching, resumes are retrieved based on **meaning and relevance**.

---

## 🤖 Multi-Agent Workflow (LangGraph)

AceAgents uses specialized AI agents working together.

```
Recruiter Query
        │
        ▼
Intent Agent
        │
        ▼
JD Parser
        │
        ▼
RAG Retriever
        │
        ▼
Candidate Analyzer
        │
        ▼
Final Hiring Recommendation
---

---


# 🧠 AI Agents

### 🎯 Intent Detection Agent

Determines recruiter intent:

* Find candidates
* Compare candidates
* Skill gap analysis
* Hiring recommendation

---

### 📄 JD Parsing Agent

Extracts structured hiring requirements from raw job descriptions.

Example:

```
Role:
Backend AI Engineer

Must Have:
- Python
- SQL
- AWS

Nice To Have:
- Docker
- Kubernetes

Experience:
2+ Years
```

---

### 🔍 Candidate Retrieval Agent (RAG)

Uses semantic embeddings to retrieve the most relevant candidates from the resume database.

Technologies:

* Sentence Transformers
* ChromaDB
* Semantic Similarity Search

---

### 👤 Candidate Analysis Agent

Analyzes every retrieved resume and scores candidates based on:

* Skill Match
* Experience
* Education
* Projects
* Certifications
* Overall Fit

Provides strengths, weaknesses, and hiring insights.

---

### 📈 Market Trend Analysis Agent

Analyzes current hiring trends for the requested role.

Provides:

* Trending technologies
* Emerging skills
* Missing in current JD
* Industry recommendations

Example:

```
Trending Skills

✅ Python
✅ Docker
✅ Kubernetes
✅ LangGraph
✅ Vector Databases
```

---

### 💡 Final Recommendation Agent

Combines outputs from all agents to generate:

* Best candidate
* Hiring confidence
* Skill gaps
* Interview recommendations
* Final justification

---

# ⚡ Tech Stack

## AI

* LangGraph
* LangChain
* OpenAI GPT
* Sentence Transformers

---

## Retrieval

* ChromaDB
* RAG
* Semantic Search

---

## Backend

* Python
* FastAPI (Ready for API integration)

---

## Data Processing

* PyPDF
* Resume Parser
* JSON

---

## Development

* Git
* GitHub

---
---

# 🚀 Workflow

```

Recruiter enters Job Description
            │
            ▼
JD Parsing
            │
            ▼
Resume Retrieval (RAG)
            │
            ▼
Candidate Analysis
            │
            ▼
Candidate Ranking
            │
            ▼
Hiring Recommendation
```

---

# 🎯 Example Use Case

**Recruiter Input**

```
Need a Backend AI Engineer

Must Have:
- Python
- SQL
- AWS

Experience:
2+ Years
```

AceAgents automatically:

✅ Parses the JD

✅ Searches the resume database

✅ Retrieves top matching candidates

✅ Scores each candidate

✅ Compares shortlisted candidates

✅ Identifies missing skills

✅ Suggests trending technologies

✅ Recommends the best hire

---

# 💡 Why AceAgents?

Traditional recruitment:

* Manual resume screening
* Keyword matching
* Time-consuming
* Biased decisions

AceAgents:

* AI-powered semantic search
* Multi-agent reasoning
* Explainable recommendations
* Objective candidate comparison
* Live market skill insights
* Faster hiring decisions

---

# 🔮 Future Enhancements

* ATS (Applicant Tracking System) Integration
* Interview Question Generation
* AI Resume Improvement Suggestions
* Candidate Fit Score Dashboard
* Recruiter Analytics Dashboard
* Multi-language Resume Support

---

# 👥 Team

**AceAgents** was built as a collaborative hackathon project focused on leveraging **Generative AI**, **RAG**, and **Multi-Agent Systems** to modernize recruitment workflows.

---

# 🏆 Key Highlights

* 🤖 Multi-Agent AI Architecture
* 📚 Retrieval-Augmented Generation (RAG)
* 🔍 Semantic Resume Search
* 📊 Candidate Ranking
* 💡 Explainable Hiring Recommendations
* ⚡ Modular & Scalable LangGraph Workflow
* 🚀 Production-ready Architecture for AI Recruitment Assistants

---

## ⭐ If you like this project, don't forget to **star the repository** and support the team!
