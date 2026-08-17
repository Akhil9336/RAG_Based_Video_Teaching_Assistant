import requests

from rag_retrieval import retrieve_chunks
from generate_prompt import create_rag_prompt


def generate_answer(question):

    # 1. Retrieve relevant chunks
    top_results = retrieve_chunks(
        question,
        top_k=5
    )

    # 2. Create context
    context = ""

    for _, row in top_results.iterrows():

        context += f"""
Tutorial: {row['tutorial_number']}
Video: {row['video_file']}
Chunk: {row['chunk_id']}
Start Time: {row['start_time']}
End Time: {row['end_time']}
Similarity: {row['similarity']:.4f}
Text: {row['text']}

"""

    # 3. Create RAG prompt
    prompt = create_rag_prompt(
        question,
        context
    )

    # 4. Send prompt to Ollama LLM
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    # 5. Return final answer
    return response.json()["response"]


# Ask user
question = input("\nAsk your question: ")

answer = generate_answer(question)

print("\n" + "=" * 80)
print("RAG ANSWER")
print("=" * 80)

print(answer)