import whisper
import os
import json

model = whisper.load_model("small")

audio_folder = "audios"
output_folder = "transcripts"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(audio_folder):

    if not file.lower().endswith(".mp3"):
        continue

    audio_path = os.path.join(audio_folder, file)

    print(f"\nProcessing: {file}")

    result = model.transcribe(
        audio_path,
        language="en",
        task="transcribe",
        fp16=False
    )

    text = result["text"]

    file_name = os.path.splitext(file)[0]
    output_path = os.path.join(
        output_folder,
        file_name + ".txt"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Saved: {output_path}")

print("\nAll tutorials have been transcribed successfully!")

