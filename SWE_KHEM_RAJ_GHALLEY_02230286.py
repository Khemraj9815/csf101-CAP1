import os
import shutil

source_directory = "/home/khemrajghalley/Downloads" #where your music, video, picture, and document files are currently located.

# Specify the destination directories for music and video files
music_destination = "/home/khemrajghalley/Music"   # wher you want to 
video_destination = "/home/khemrajghalley/Videos"   # where you want to organize and move the files based on their types.
picture_destination = "/home/khemrajghalley/Pictures"
document_destination = "/home/khemrajghalley/Documents"

# Create the destination directories if they don't exist
for directory in [music_destination, video_destination, picture_destination, document_destination]:
    if not os.path.exists(directory):
        os.mkdir(directory)

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    source_file = os.path.join(source_directory, filename)
    
    # Check if it's a music file (you can add more extensions if needed)
    if filename.endswith((".mp3", ".wav", ".flac")):
        # Move music files to the music destination
        shutil.move(source_file, os.path.join(music_destination, filename))
    
    # Check if it's a video file (you can add more extensions if needed)
    elif filename.endswith((".mp4", ".avi", ".mkv")):
        # Move video files to the video destination
        shutil.move(source_file, os.path.join(video_destination, filename))
    
    elif filename.endswith(("jpg")):
        #Move picture files to the picture destination
        shutil.move(source_file, os.path.join(picture_destination, filename))

    elif filename.endswith(("pdf")):
        #Move pdf files to the document destination
        shutil.move(source_file, os.path.join(document_destination, filename))

print("File organization completed.")
