"""
vector_store.py
Purpose: Create a Chroma database, embed all resumes, and store them.
"""
import chromadb
from rag.loader import load_resumes
from rag.embedding import create_embedding

# Initialize ChromaDB client (stores data in memory for now)
client = chromadb.Client()
collection = client.get_or_create_collection(name="resumes")

def build_database():
    print("Loading resumes into database... this might take a few seconds.")
    resumes = load_resumes()
    
    for resume in resumes:
        # Convert the resume text into a vector
        embedding = create_embedding(resume["text"])
        
        # Save to ChromaDB
        collection.add(
            ids=[resume["id"]],
            documents=[resume["text"]],
            embeddings=[embedding]
        )
    print("✅ Database Ready! All 20 resumes are indexed.")

# Run this to test if the file is executed directly
if __name__ == "__main__":
    build_database()