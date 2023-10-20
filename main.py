from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
from gtts import gTTS
from playsound import playsound
import os


class run:
    def __init__(self):
        # GUI Screen
        self.root = Tk()
        self.root.title("Language - Translator")
        self.root.geometry("1040x500")
        self.root.resizable(False, False)
        self.root.config(bg='#b2c2cf')
        self.top_frame = Frame(self.root, bg="white", width=1020, height=15)
        self.top_frame.place(x=0, y=0)

        # Calling Widgets Function
        self.placing_widgets()
        self.root.mainloop()

    def placing_widgets(self):

        # Language List
        self.languages = googletrans.LANGUAGES
        self.language_list = list(self.languages.values())

        # Text Boxes
        self.original_text = Text(
            self.root, height=10, width=40, bg="#ffffff", font=("Times New Roman", 15))
        self.original_text.grid(row=1, column=1, pady=20, padx=10)

        self.translated_text = Text(
            self.root, height=10, width=40, bg="#ffffff", font=("Times New Roman", 15))
        self.translated_text.grid(row=1, column=3, pady=20, padx=10)

        # Buttons
        self.translated_button = Button(self.root, text="Translate!", font=(
            "Helvetica", 20), command=self.translate_it, bg="#4db4d6", fg="black")
        self.translated_button.grid(row=1, column=2, padx=15)

        self.input_button = Button(self.root, text="Voice_input", font=(
            "Helvetica", 20), command=self.input, bg='#4db4d6')
        self.input_button.grid(row=4, column=1, padx=10)

        self.translated_button = Button(self.root, text="Voice_output", font=(
            "Helvetica", 20), command=self.Speak, bg='#4db4d6')
        self.translated_button.grid(row=4, column=3, padx=10)

        # combo Boxes
        self.original_combo = ttk.Combobox(
            self.root, width=50, value=self.language_list)
        self.original_combo.current(21)
        self.original_combo.grid(row=2, column=1)

        self.translated_combo = ttk.Combobox(
            self.root, width=50, value=self.language_list)
        self.translated_combo.current(38)
        self.translated_combo.grid(row=2, column=3)

        # clear Button
        self.clear_btn = Button(
            self.root, text="Clear", command=self.clear, bg='#4db4d6', width=6, height=2)
        self.clear_btn.grid(row=3, column=2)

    # Translation
    def translate_it(self):

        self.translated_text.delete(1.0, END)
        try:
            for key, value in self.languages.items():
                if (value == self.original_combo.get()):
                    from_language_key = key

            for key, value in self.languages.items():
                if (value == self.translated_combo.get()):
                    to_language_key = key

            words = textblob.TextBlob(self.original_text.get(1.0, END))

            words = words.translate(
                from_lang=from_language_key, to=to_language_key)

            self.translated_text.insert(1.0, words)

        except Exception as e:
            messagebox.showerror("Translator", e)

    # Taking Input From Mic
    def input(self):

        for key, value in self.languages.items():
            if (value == self.original_combo.get()):
                from_language_key = key

        import speech_recognition as sr
        self.r = sr.Recognizer()

        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=0.3)
            print("Speak now")

            audio = self.r.listen(source)

            try:
                self.text = self.r.recognize_google(
                    audio, language=from_language_key)
                self.original_text.insert(1.0, self.text)

            except:
                messagebox.showerror('Not Recognized', 'Please say again')

    # Output Through Speaker
    def Speak(self):

        for key, value in self.languages.items():
            if (value == self.translated_combo.get()):
                to_language_key = key

        words = self.translated_text.get(1.0, END)
        # Converting text into a mp3 File
        obj = gTTS(text=words, slow=False, lang=to_language_key)
        obj.save('captured_voice.mp3')

        # Playing the convertedmp3 File
        playsound("E:\\projects\\Translator\\captured_voice.mp3")

        # Removing the mp3 File After Playing
        os.remove("E:\\projects\\Translator\\captured_voice.mp3")

    # Clearing All The Inputed And Outputed Text
    def clear(self):
        self.original_text.delete(1.0, END)
        self.translated_text.delete(1.0, END)


# Creating Object
obj = run()
