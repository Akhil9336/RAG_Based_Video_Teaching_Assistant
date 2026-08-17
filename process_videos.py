import os
import subprocess

files =os.listdir("videos")
for file in files:
    print(file)
    # Remove .mp4 from filename
    file_name = os.path.splitext(file)[0]

    # Extract tutorial number
    tutorial_number = file_name.split("#")[1]
    
   
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])