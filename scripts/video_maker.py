from moviepy.editor import *
import os

def make_video(images_folder, audio_file, output_file):
    clips = [ImageClip(f"{images_folder}/{img}").set_duration(3) for img in os.listdir(images_folder)]
    video = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip(audio_file)
    video = video.set_audio(audio)
    video.write_videofile(output_file, fps=24)

if __name__ == "__main__":
    make_video("images/beyoncé", "voice.mp3", "output.mp4")





#     from moviepy.editor import *
# import os

# def create_video(image_files, audio_file, output_path):
#     clips = []
#     duration_per_image = 3  # seconds
#     for img in image_files:
#         clip = ImageClip(img).set_duration(duration_per_image)
#         clips.append(clip)
#     video = concatenate_videoclips(clips, method="compose")
#     audio = AudioFileClip(audio_file)
#     video = video.set_audio(audio)
#     video.write_videofile(output_path, fps=24)

# if __name__ == "__main__":
#     images = [f"images/image_{i}.jpg" for i in range(1, 6)]
#     audio_path = "voice/voice.mp3"
#     output_video = "videos/output_video.mp4"
#     create_video(images, audio_path, output_video)