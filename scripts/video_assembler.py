from moviepy.editor import *
import os

def create_video(image_folder="images", audio_file="voice.mp3", output="output.mp4"):
    images = [f"{image_folder}/{img}" for img in os.listdir(image_folder)]
    clips = [ImageClip(img).set_duration(3) for img in images]
    video = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip(audio_file)
    video = video.set_audio(audio)
    video.write_videofile(output, fps=24)

if __name__ == "__main__":
    create_video()