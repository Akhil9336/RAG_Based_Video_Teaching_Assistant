import requests
import joblib
import numpy as np


def create_embedding(text):

    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": "bge-m3",
            "prompt": text
        }
    )

    response.raise_for_status()

    return response.json()["embedding"]


def cosine_similarity(a, b):

    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


def retrieve_chunks(query, top_k=5):

    # Load saved DataFrame
    df = joblib.load("video_embeddings.pkl")

    # Create embedding for question
    query_embedding = create_embedding(query)

    # Calculate similarity
    df["similarity"] = df["embedding"].apply(
        lambda x: cosine_similarity(query_embedding, x)
    )

    # Get top results
    top_results = df.sort_values(
        by="similarity",
        ascending=False
    ).head(top_k)

    return top_results