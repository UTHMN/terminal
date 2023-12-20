from pytube import *
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

def Download():
    link = input("Enter the YouTube video URL: ")

    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    video = YouTube(f"{link}")
    try:
        youtubeObject.download()
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f"{video.title}.mp3")

        title = input("Enter a title: ")
        # Open the video and audio
        video_clip = VideoFileClip(f"{video.title}.mp4")
        audio_clip = AudioFileClip(f"{video.title}.mp3")
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(title + ".mp4")

        mode = input("Successfully Merged audio to video, delete original files? ")
        if mode == "Yes":
            if os.path.exists(f"{video.title}.mp4") and os.path.exists(f"{video.title}.mp3"):
                os.remove(f"{video.title}.mp4")
                os.remove(f"{video.title}.mp3")
            else:
                print("The file does not exist") 
        elif mode == "No":
            pass
        else:
            pass

    except:
        print("An error has occurred")
    print("Download is completed successfully")