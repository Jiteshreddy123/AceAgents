# 🚀 AceAgents – Multi-Agent AI Recruitment Assistant

> **Hire smarter, faster, and more objectively with AI-powered recruitment.**

AceAgents is a **Multi-Agent Recruitment Intelligence System** that automates candidate screening using AI agents, RAG (Retrieval-Augmented Generation), semantic search, and live market insights.

Instead of manually reviewing hundreds of resumes, recruiters simply provide a Job Description. AceAgents then performs intelligent candidate retrieval, evaluation, ranking, comparison, and hiring recommendations.

---

## 🎥 Project Demo

📹 **Demo Video (Google Drive):** [Watch the Demo Video](https://drive.google.com/file/d/1tfMIclEuXLGseUllI_fjpx956PJvwtT1/view?usp=sharing)

---

## ✨ Features

### 📄 AI Job Description Parser
Converts unstructured JDs into structured hiring requirements by extracting:
* Required Skills
* Preferred Skills
* Experience
* Education
* Role

### 📚 Resume Knowledge Base (RAG)
* Parses resumes into structured candidate profiles.
* Creates vector embeddings and stores them in ChromaDB.
* Performs semantic candidate retrieval based on **meaning and relevance** instead of basic keyword matching.

### 🤖 Multi-Agent Workflow (LangGraph)
AceAgents uses specialized AI agents working together seamlessly:

```text
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
```

---

## 🧠 AI Agents

### 🎯 Intent Detection Agent
Determines the recruiter's exact intent:
* Find candidates
* Compare candidates
* Skill gap analysis
* Hiring recommendation

### 📄 JD Parsing Agent
Extracts structured hiring requirements from raw job descriptions. 
*Example Output:*
```text
Role: Backend AI Engineer

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

### 🔍 Candidate Retrieval Agent (RAG)
Uses semantic embeddings to retrieve the most relevant candidates from the resume database.
* **Technologies:** Sentence Transformers, ChromaDB, Semantic Similarity Search

### 👤 Candidate Analysis Agent
Analyzes every retrieved resume and scores candidates based on skill match, experience, education, projects, certifications, and overall fit. Provides strengths, weaknesses, and hiring insights.

### 📈 Market Trend Analysis Agent
Analyzes current hiring trends for the requested role to provide trending technologies, emerging skills, and industry recommendations.
*Example Output:*
```text
Trending Skills:
✅ Python
✅ Docker
✅ Kubernetes
✅ LangGraph
✅ Vector Databases
```

### 💡 Final Recommendation Agent
Combines outputs from all agents to generate the best candidate match, hiring confidence, skill gaps, interview recommendations, and final justification.

---

## ⚡ Tech Stack

| Category | Technologies |
| :--- | :--- |
| **AI Architecture** | LangGraph, LangChain, OpenAI GPT, Sentence Transformers |
| **Retrieval & DB** | ChromaDB, RAG, Semantic Search |
| **Backend** | Python, FastAPI *(Ready for API integration)* |
| **Data Processing** | PyPDF, Resume Parser, JSON |
| **Development** | Git, GitHub |

---

## 🚀 Workflow

```text
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

## 🎯 Example Use Case

**Recruiter Input:**
```text
Need a Backend AI Engineer

Must Have:
- Python
- SQL
- AWS

Experience:
2+ Years
```

**AceAgents automatically:**
* ✅ Parses the JD
* ✅ Searches the resume database
* ✅ Retrieves top matching candidates
* ✅ Scores each candidate
* ✅ Compares shortlisted candidates
* ✅ Identifies missing skills
* ✅ Suggests trending technologies
* ✅ Recommends the best hire

---

## 💡 Why AceAgents?

* **Traditional Recruitment:** Manual resume screening, rigid keyword matching, time-consuming processes, and biased decisions.
* **AceAgents:** AI-powered semantic search, multi-agent reasoning, explainable recommendations, objective candidate comparison, live market skill insights, and faster hiring decisions.

---

## 🔮 Future Enhancements

* ATS (Applicant Tracking System) Integration
* Automated Interview Question Generation
* AI Resume Improvement Suggestions for candidates
* Candidate Fit Score Dashboard
* Recruiter Analytics Dashboard
* Multi-language Resume Support

---

## 👥 Team & Highlights

**AceAgents** was built as a collaborative hackathon project focused on leveraging **Generative AI**, **RAG**, and **Multi-Agent Systems** to modernize recruitment workflows.

### 🏆 Key Highlights
* 🤖 Multi-Agent AI Architecture
* 📚 Retrieval-Augmented Generation (RAG)
* 🔍 Semantic Resume Search
* 📊 Candidate Ranking & Explainable Hiring Recommendations
* ⚡ Modular & Scalable LangGraph Workflow

---

## ⭐ If you like this project, don't forget to star the repository and support the team!
