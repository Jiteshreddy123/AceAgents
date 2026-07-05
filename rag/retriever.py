"""
retriever.py
Purpose: Convert the HR query into a vector and search ChromaDB for the best matches.
"""
from rag.vector_store import collection
from rag.embedding import create_embedding
from rag.parser import parse_resume

def retrieve_candidates(query: str, top_n: int = 5):
    print(f"Searching database for: '{query}'...")
    
    # 1. Convert the HR's search text into a 384-length vector
    query_embedding = create_embedding(query)
    
    # 2. Ask ChromaDB for the closest matching resumes
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_n
    )
    
    return results
import re

def search_candidates(query: str):
    
    # Default value
    top_k = 5

    # Look for a number in the query
    match = re.search(r"\b(\d+)\b", query)

    if match:
        top_k = int(match.group(1))

    # Prevent invalid values
    top_k = max(1, min(top_k, 20))

    raw_results = retrieve_candidates(query, top_n=top_k)

    final_candidates = []

    for i in range(len(raw_results["ids"][0])):

        candidate_id = raw_results["ids"][0][i]
        resume_text = raw_results["documents"][0][i]
        distance_score = raw_results["distances"][0][i]

        structured_data = parse_resume(resume_text)

        match_percentage = round(
            max(0, (2.0 - distance_score) / 2.0 * 100),
            1
        )

        structured_data["match_score"] = f"{match_percentage}%"
        structured_data["candidate_id"] = candidate_id

        final_candidates.append(structured_data)

    return final_candidates