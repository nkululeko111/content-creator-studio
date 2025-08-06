from gtts import gTTS
import os

def text_to_speech(text, output_file="voice.mp3"):
    tts = gTTS(text, lang="en", slow=False)
    tts.save(output_file)

if __name__ == "__main__":
    text = "Allegedly, Beyoncé was spotted in Cape Town..."
    text_to_speech(text)