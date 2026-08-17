import requests
import joblib
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

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


# Load saved DataFrame
df = joblib.load("video_embeddings.pkl")

print("Total chunks:", len(df))


# Ask user for a question
query = input("\nAsk your question: ")


# Create embedding for question
query_embedding = create_embedding(query)


# Calculate similarity
df["similarity"] = df["embedding"].apply(
    lambda x: cosine_similarity(query_embedding, x)
)


# Get top 5 results
top_results = df.sort_values(
    by="similarity",
    ascending=False
).head(5)


# Display results
print("\n" + "=" * 80)
print("TOP MATCHING RESULTS")
print("=" * 80)

for rank, (_, row) in enumerate(top_results.iterrows(), start=1):

    print(f"\nRank: {rank}")
    print(f"Tutorial: {row['tutorial_number']}")
    print(f"Video: {row['video_file']}")
    print(f"Chunk ID: {row['chunk_id']}")
    print(f"Start Time: {row['start_time']}")
    print(f"End Time: {row['end_time']}")
    print(f"Similarity Score: {row['similarity']:.4f}")
    print(f"Text: {row['text']}")
    print("-" * 80)