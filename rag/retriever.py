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
def search_candidates(query: str, top_k: int = 5):
    """
    The main function Surya will call to get structured candidate data.
    """
    raw_results = retrieve_candidates(query, top_n=top_k)
    
    final_candidates = []
    # Loop through the results and format them
    for i in range(len(raw_results["ids"][0])):
        candidate_id = raw_results["ids"][0][i]
        resume_text = raw_results["documents"][0][i]
        distance_score = raw_results["distances"][0][i]
        
        # Parse the text into a clean dictionary
        structured_data = parse_resume(resume_text)
        
        # Add the match score (converting distance to a mock percentage for display)
        match_percentage = round(max(0, (2.0 - distance_score) / 2.0 * 100), 1)
        structured_data["match_score"] = f"{match_percentage}%"
        structured_data["candidate_id"] = candidate_id
        
        final_candidates.append(structured_data)
        
    return final_candidates