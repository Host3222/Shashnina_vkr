import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
from vosk import Model, KaldiRecognizer
import speech_recognition
import wave
import json
import os
from googletrans import Translator, constants
import gtts
from gtts import gTTS
import os
global str
import tkinter.ttk as ttk
from playsound import playsound
from PIL import Image
from PIL import ImageTk, Image


master = tk.Tk()
master.image = PhotoImage(file='1.png')
bg_log = Label(master, image=master.image)
bg_log.grid(row=0, column=0)

def buttonCallback():

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    with microphone:
        recognized_data = ""

        try:
            print("слушаю...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("проверте подключение микрофона")
            return
        try:
            print("начало записи...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        return recognized_data


def buttonCallback2():
    while True:
        voice_input = buttonCallback()




        print(voice_input)
        translator = Translator()
        global Port
        Port = combo2.get()
        translation = translator.translate(voice_input, dest=Port)
        print(f"{translation.text} ({translation.dest})")

#История

        text_val = f"{translation.text}"
        f = open('history.txt', 'a')
        f.write("Переведенное: " +(text_val) + "  оригинал:  " + (voice_input) + '\n')
        f.close()
        lbl.config(text=text_val)
        #lbl1.config(text=voice_input)
        master.update()


        obj = gTTS(text=text_val, slow=False)
        obj.save("exam.mp3")
        playsound("exam.mp3")
        os.remove("exam.mp3")



def openfile():
    f = open("history.txt", "r")
    print(*f)

def buttonCallback():

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    with microphone:
        recognized_data = ""

        try:
            print("Слушаю...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("проверте подключение микрофона")
            return
        try:
            print("начало записи...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        return recognized_data


def buttonCallback4():
    while True:
        voice_input = buttonCallback()

        print(voice_input)
        translator = Translator()
        global Port
        Port = combo2.get()
        translation = translator.translate(voice_input, dest=Port)
        print(f"{translation.text} ({translation.dest})")

#История

        text_val = f"{translation.text}"
        f = open('history.txt', 'a')
        f.write("Переведенное: " +(text_val) + "  оригинал:  " + (voice_input) + '\n')
        f.close()
        lbl.config(text=text_val)
        #lbl1.config(text=voice_input)
        master.update()


        obj = gTTS(text=text_val, slow=False)


button2 = tk.Button(master, text="Озвученный суфлер", command=buttonCallback2)

button2.grid(row=9, column=0)
button2.place(x=260, y=90)
lbl = Label(master, text="난 게이야", font=("Arial Bold", 15))
#lbl1 = Label(master, text="Привет, тут будет оригинал", font=("Arial Bold", 15))

lbl.grid(column=0, row=0)
lbl.place(x=70, y=150)
#lbl1.grid(column=0, row=1)
#lbl1.place(x=0, y=200)

combo2 = Combobox(master)
combo2.grid(column=0, row=4)
combo2.place(x=0, y=30)
combo2['values'] = ("ru", "en", "es", "ja", "la")


button3 = tk.Button(master, text="История", command=openfile)
button3.grid(row=50, column=0)
button3.place(x=260, y=30)

button4 = tk.Button(master, text="Суфлер", command=buttonCallback4)

button4.grid(row=9, column=0)
button4.place(x=260, y=60)

tk.mainloop()

