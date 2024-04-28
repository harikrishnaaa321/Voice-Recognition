import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox
import threading

def Speech_to_Text():
    global listening_thread
    listening_thread = threading.Thread(target=continuous_speech_recognition)
    listening_thread.start()
def continuous_speech_recognition():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            txtSpeech.insert(tk.END, "Speaker: " + text + "\n")
            if text.lower() == 'quit':
                txtSpeech.insert(tk.END, "Exiting the program...\n")
                break
        except sr.UnknownValueError:
            txtSpeech.insert(tk.END, "Sorry, I didn't catch that. Please try again.\n")
        except sr.RequestError:
            txtSpeech.insert(tk.END, "Sorry, I couldn't reach the Google API.\n")

def reset_txtSpeech():
    txtSpeech.delete("1.0", tk.END)

def exit_system():
    result = messagebox.askquestion("Exit system", "Confirm if you want to exit")
    if result == 'yes':
        messagebox.showinfo("Goodbye", "Goodbye")
        root.destroy()

root = tk.Tk()
root.title("Speech to Text")
MainFrame = tk.Frame(root, bd=20, width=700, height=400)
MainFrame.pack()
lblTitle = tk.Label(MainFrame, font=('arial', 30, 'bold'), text="Speech to Text", width=15)
lblTitle.pack()
txtSpeech = tk.Text(MainFrame, font=('arial', 20), width=68, height=12)
txtSpeech.pack()
btnConvert = tk.Button(MainFrame, font=('arial', 20), text="Start Listening", width=18, height=2,
                       command=Speech_to_Text)
btnConvert.pack(side=tk.LEFT, padx=5)
btnReset = tk.Button(MainFrame, font=('arial', 20), text="Reset", width=18, height=2,
                     command=reset_txtSpeech)
btnReset.pack(side=tk.LEFT, padx=5)
btnExit = tk.Button(MainFrame, font=('arial', 20), text="Exit", width=18, height=2,
                    command=exit_system)
btnExit.pack(side=tk.LEFT, padx=5)
root.mainloop()
