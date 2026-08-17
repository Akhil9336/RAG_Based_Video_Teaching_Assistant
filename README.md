# 🎓 RAG-Based Video Teaching Assistant

> An AI-powered video learning assistant that helps learners find **where a particular topic is taught**, **which tutorial contains it**, and **approximately where to start watching**.

---

## 📌 Overview

Finding a specific concept inside multiple long educational videos can be time-consuming.

The **RAG-Based Video Teaching Assistant** solves this problem by converting educational videos into searchable knowledge.

Users can ask questions such as:

> "Where is Tableau taught?"

Instead of manually searching through every video, the system retrieves the most relevant video chunks and provides:

- 📚 The relevant tutorial
- 🎥 The video filename
- 🕐 Approximate timestamp
- 📝 What is taught in that section
- 📊 How much of the topic is covered
- ▶️ Which video the learner should watch

The project uses **Retrieval-Augmented Generation (RAG)** to combine semantic search with an AI language model.

---

## 🎯 Problem Statement

Educational courses often contain multiple long videos covering different concepts.

When a learner wants to revise a particular topic, they may have to:

1. Open multiple videos
2. Search manually through the content
3. Identify the relevant section
4. Remember where the topic was explained

This process is inefficient and time-consuming.

### 💡 Proposed Solution

Build an AI-powered system that understands the content of educational videos and allows users to search them using natural language.

The system retrieves the most relevant video segments and guides the learner directly to the appropriate tutorial and timestamp.

---

# ⚙️ System Workflow

```text
                Educational Videos
                       │
                       ▼
                    FFmpeg
                       │
                       ▼
                  Audio Files
                       │
                       ▼
                    Whisper
                       │
                       ▼
                 Transcriptions
                       │
                       ▼
              Chunking + Metadata
                       │
                       ▼
               Video Chunks JSON
                       │
                       ▼
              Ollama + BGE-M3
                       │
                       ▼
                  Embeddings
                       │
                       ▼
             Saved Vector Data
                       │
                       ▼
                 User Question
                       │
                       ▼
               Query Embedding
                       │
                       ▼
              Similarity Search
                       │
                       ▼
             Top Relevant Chunks
                       │
                       ▼
                  RAG Prompt
                       │
                       ▼
                   LLM / Ollama
                       │
                       ▼
              Context-Aware Answer
