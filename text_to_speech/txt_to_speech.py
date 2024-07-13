from gtts import gTTS
import os

text = ("Hello guys, I have built this text-to-speech converter in Python. "
        "Development in Python is really fast and easy as it provides tons of libraries. "
        "You can also create a text-to-speech converter in JavaScript. "
        "I am dropping the code and tutorial for creating text-to-speech converter in JavaScript below.")

language = 'en'

try:
    speak = gTTS(text=text, lang=language, slow=False)
    speak.save('result.mp3')
    os.system('result.mp3')
    print("Text-to-speech conversion successful. The audio file has been saved as 'result.mp3'.")
except Exception as e:
    print(f"An error occurred: {e}")
