import pyttsx3

def text_to_speech(text, output_file="voice.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

if __name__ == "__main__":
    text = "Allegedly, Kenny Kunene was seen at a private party in Johannesburg..."
    text_to_speech(text)