# Retrieval-Augmented Generation (RAG) Module

This module handles the core vector database and semantic search for the AceAgents recruitment platform. 

### Architecture
* **`loader.py`**: Ingests 20 varied, realistic AI Engineer resumes from the `data/` folder.
* **`embedding.py`**: Utilizes `sentence-transformers` (`all-MiniLM-L6-v2`) to convert resume text into 384-dimensional mathematical vectors.
* **`vector_store.py`**: Initializes an in-memory ChromaDB instance to store and index candidate embeddings.
* **`retriever.py`**: Takes natural language queries, converts them to vectors, and performs similarity searches against the ChromaDB collection.
* **`parser.py`**: Extracts structured metadata (Name, Experience, Skills) from raw text for Explainable AI output.

### Usage
```python
from rag.retriever import search_candidates

# Returns top 5 matched candidates as structured JSON/Dictionaries
results = search_candidates("Python FastAPI Docker AWS", top_k=5)