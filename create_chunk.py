import os
import json
import whisper

model = whisper.load_model("small")

audio_folder = "audios"
output_file = "mp3_chunks.json"

all_chunks = []

for file in os.listdir(audio_folder):

    if not file.lower().endswith(".mp3"):
        continue

    audio_path = os.path.join(audio_folder, file)

    print(f"Processing: {file}")

    result = model.transcribe(
        audio_path,
        language="en",
        task="transcribe",
        fp16=False
    )

    # Get Whisper segments
    for i, segment in enumerate(result["segments"]):

        chunk = {
            "audio_file": file,
            "chunk_id": i,
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"].strip()
        }

        all_chunks.append(chunk)

# Write chunks to JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=4, ensure_ascii=False)

print(f"\nChunks saved successfully to {output_file}")