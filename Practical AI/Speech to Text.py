import speech_recognition as sr

r=sr.Recognizer()

File="Harvard.wav"

with sr.AudioFile(File) as source:
    audio_data=r.record(source)
    text=r.recognize_google(audio_data)

print(text)
