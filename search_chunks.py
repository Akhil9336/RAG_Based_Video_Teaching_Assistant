import requests
import pandas as pd
import numpy as np


# Create embedding for the user's question
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


# Calculate cosine similarity
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Load our stored chunks and embeddings
df = pd.read_pickle("video_embeddings.pkl")

print("Total chunks loaded:", len(df))


# User's question
query = input("\nAsk your question: ")


# Create embedding for the question
query_embedding = create_embedding(query)


# Calculate similarity with every chunk
df["similarity"] = df["embedding"].apply(
    lambda x: cosine_similarity(query_embedding, x)
)


# Get top 5 matching chunks
top_chunks = df.sort_values(
    by="similarity",
    ascending=False
).head(5)


print("\nTop Matching Chunks:\n")

for _, row in top_chunks.iterrows():

    print("=" * 70)

    print("Tutorial:", row["tutorial_number"])
    print("Video:", row["video_file"])
    print("Chunk:", row["chunk_id"])
    print("Start:", row["start_time"])
    print("End:", row["end_time"])
    print("Similarity:", round(row["similarity"], 4))
    print("Text:", row["text"])