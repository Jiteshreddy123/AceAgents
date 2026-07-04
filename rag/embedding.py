"""
embedding.py

Purpose:
--------
Convert resume text or job description into vector embeddings.

We use the free SentenceTransformer model:
all-MiniLM-L6-v2


Output:
384-dimensional embedding vector
"""

from sentence_transformers import SentenceTransformer

# ----------------------------------------------------
# Load embedding model only once
# ----------------------------------------------------

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded successfully!\n")


# ----------------------------------------------------
# Create embedding
# ----------------------------------------------------

def create_embedding(text: str):
    """
    Convert text into a vector embedding.

    Parameters
    ----------
    text : str
        Resume text or JD text.

    Returns
    -------
    list
        384-dimensional embedding vector.
    """

    embedding = model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding.tolist()


# ----------------------------------------------------
# Batch embedding
# ----------------------------------------------------

def create_embeddings(texts: list):
    """
    Convert multiple texts into embeddings.

    Parameters
    ----------
    texts : list[str]

    Returns
    -------
    list
        List of embeddings
    """

    embeddings = model.encode(
        texts,
        convert_to_numpy=True
    )

    return embeddings.tolist()


# ----------------------------------------------------
# Test
# ----------------------------------------------------

if __name__ == "__main__":

    sample = """
    Python
    FastAPI
    Docker
    AWS
    LangChain
    """

    vector = create_embedding(sample)

    print("=" * 60)
    print("Embedding Created")
    print("=" * 60)

    print(f"\nVector Dimension : {len(vector)}")

    print("\nFirst 10 Values:")

    print(vector[:10])