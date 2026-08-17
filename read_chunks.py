import requests
import pandas as pd
import joblib


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


# Read video chunks
df = pd.read_json("video_chunks.json")

print("Total chunks:", len(df))
print(df.head())


# Create embeddings for every chunk
df["embedding"] = df["text"].apply(create_embedding)


# Save DataFrame using Joblib
joblib.load(df, "video_embeddings.pkl")

print("\nEmbeddings created successfully!")
print("Total embeddings:", len(df))
print("Embedding size:", len(df["embedding"].iloc[0]))
print("DataFrame saved successfully using Joblib!")
