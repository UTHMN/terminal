import re
from pytube import *
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import filemodifer

def Download():
    try:
        link = input("Enter the YouTube video URL: ")
        choice = input("Audio, Video or Video + Audio: ")

        if choice.lower() == "video + audio":
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            video = YouTube(f"{link}")
            vtitle = re.sub(r'[^\w]', ' ', video.title) # Removes symbols

            stream = video.streams.filter(only_video=True).first()
            stream.download(filename=f"{vtitle}.mp4")
            stream = video.streams.filter(only_audio=True).first()
            stream.download(filename=f"{vtitle}.mp3")

            title = "youtube_export"
            # Open the video and audio
            video_clip = VideoFileClip(f"{vtitle}.mp4")
            audio_clip = AudioFileClip(f"{vtitle}.mp3")
            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(title + ".mp4")

            files = [f"{vtitle}.mp4", f"{vtitle}.mp3", "youtube_exportTEMP_MPY_wvf_snd.mp3"]
            filemodifer.removebatch(files)

        elif choice.lower() == "video":
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            video = YouTube(f"{link}")
            vtitle = re.sub(r'[^\w]', ' ', video.title) # Removes symbols

            stream = video.streams.filter(only_video=True).first()
            stream.download(filename=f"{vtitle}.mp4")

        elif choice.lower() == "audio":
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            video = YouTube(f"{link}")
            vtitle = re.sub(r'[^\w]', ' ', video.title) # Removes symbols

            stream = video.streams.filter(only_audio=True).first()
            stream.download(filename=f"{vtitle}.mp3")

        else:
            print("invalid mode")

        print("Download is completed successfully")

    except Exception as error:
        print(f"An error has occurred: {error}")

    