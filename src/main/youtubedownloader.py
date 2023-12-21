import re
from pytube import *
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

def Download():
    link = input("Enter the YouTube video URL: ")

    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    video = YouTube(f"{link}")
    vtitle = re.sub(r'[^\w]', ' ', video.title) # Removes symbols
    try:
        stream = video.streams.filter(only_video=True).first()
        stream.download(filename=f"{vtitle}.mp4")
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f"{vtitle}.mp3")

        title = input("Enter a title: ")
        # Open the video and audio
        video_clip = VideoFileClip(f"{vtitle}.mp4")
        audio_clip = AudioFileClip(f"{vtitle}.mp3")
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(title + ".mp4")

        mode = input("Successfully Merged audio to video, delete original files? ")
        if mode == "Yes":
            if os.path.exists(f"{vtitle}.mp4") and os.path.exists(f"{vtitle}.mp3"):
                os.remove(f"{vtitle}.mp4")
                os.remove(f"{vtitle}.mp3")
            else:
                print("The file does not exist") 
        else:
            pass

    except:
        print("An error has occurred")
    print("Download is completed successfully")
    