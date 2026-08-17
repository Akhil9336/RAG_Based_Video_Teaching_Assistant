import os
import json
import whisper

# Load Whisper model
model = whisper.load_model("small")

video_folder = "videos"
output_file = "video_chunks.json"

all_chunks = []

for file in os.listdir(video_folder):

    if not file.lower().endswith(".mp4"):
        continue

    video_path = os.path.join(video_folder, file)

    print(f"\nProcessing: {file}")

    # Transcribe video directly
    result = model.transcribe(
        video_path,
        language="en",
        task="transcribe",
        fp16=False
    )

    # Extract tutorial number
    file_name = os.path.splitext(file)[0]

    if "#" in file_name:
        tutorial_number = file_name.split("#")[1].strip()
    else:
        tutorial_number = "unknown"

    # Create chunks from Whisper segments
    for i, segment in enumerate(result["segments"]):

        chunk = {
            "tutorial_number": tutorial_number,
            "video_file": file,
            "chunk_id": i,
            "start_time": segment["start"],
            "end_time": segment["end"],
            "text": segment["text"].strip()
        }

        all_chunks.append(chunk)

# Save everything to JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(
        all_chunks,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nAll video files have been chunked successfully!")
print(f"Saved to: {output_file}")
print(f"Total chunks: {len(all_chunks)}")