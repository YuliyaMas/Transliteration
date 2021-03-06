from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from translit import *


class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.create_widgets()
        self.images()
        # self.get_text()
        self.translit_text(self)
        self.clear()

    def create_widgets(self):
        # Widgets for text in Russian
        self.label_input = tk.Label(self, text="Put here the original text", fg="SlateBlue2",
                                    bg="snow", font="Annabelle 15")
        self.text_input = tk.Text(width=110, height=20, bd=5, wrap=tk.WORD, bg="light yellow")
        self.scroll_input = tk.Scrollbar(orient="vertical", command=self.text_input.yview)
        # Pour insérer le texte original à partir du fichier :
        self.button_tr = tk.Button(self, text="Transliterate", fg="black", font="Lobster 15",
                                   command=lambda: self.translit_text(self.text_input))
        # Widgets for transliterated text
        self.label_output = tk.Label(self, text="This is the translitereted text", fg="IndianRed2", bg="snow",
                                     font="Lobster 15")
        self.text_output = tk.Text(width=110, height=20, bd=5, wrap=tk.WORD, bg="light yellow")
        self.scroll_output = tk.Scrollbar(orient="vertical", command=self.text_output.yview)
        self.button_clear = tk.Button(self, text="Clear", width=20, command=self.clear)
        self.button_quit = tk.Button(self, text="Quit", width=20, command=self.quit)
        self.rules_1 = tk.Button(self, text="Transliteration ISO-9", width=20)
        self.rules_2 = tk.Button(self, text="Transliteration RU-Latin", width=20)

        self.label_input.grid(column=1, row=0, sticky=tk.N)
        self.text_input.grid(column=1, row=0, sticky=tk.SW)
        self.scroll_input.grid(column=1, row=0, sticky=tk.E)
        self.text_input.config(yscrollcommand=self.scroll_output.set)
        self.button_tr.grid(column=1, row=1, sticky=tk.S)
        self.label_output.grid(column=1, row=2, sticky=tk.N)
        self.text_output.grid(column=1, row=2, sticky=tk.SW)
        self.scroll_output.grid(column=1, row=2, sticky=tk.E)
        self.text_output.config(yscrollcommand=self.scroll_output.set)
        self.button_clear.grid(column=2, row=0)
        self.button_quit.grid(column=2, row=2)
        self.rules_1.grid(column=1, row=1, sticky=tk.SW)
        self.rules_2.grid(column=1, row=1, sticky=tk.SE)

        self.geometry("700x300")

    # Illustrations
    def images(self):
        self.image_1 = Image.open("poo_translit/ru.jpg")
        self.photo_1 = ImageTk.PhotoImage(self.image_1)
        self.img_1 = tk.Label(image=self.photo_1, width=450, height=450)
        self.img_1.image = self.photo_1
        self.img_1.grid(rowspan=2, column=0, row=0)
        self.image_2 = Image.open("poo_translit/lat.jpg")
        self.photo_2 = ImageTk.PhotoImage(self.image_2)
        self.img_2 = tk.Label(image=self.photo_2, width=450, height=450)
        self.img_2.image = self.photo_2
        self.img_2.grid(rowspan=2, column=0, row=2)

    # Transliteration
    def translit_text(self, texte):
        # self.text_input.delete(1.0, END)
        try:
            t = Translitteration()
            texte = self.text_input.get(1.0, END)
            if "а" or "б" or "в" or "г" or "д" or "е" or "ж" or "з" or "и" or "к" or "л" or "м" or "н" or "о" or "п" or \
                    "р" or "с" or "т" or "у" or "ф" or "х" or "ц" or "ч" or "ш" or "щ" or "ы" or "э" or "ю" or "я" in texte:
                # INPUT = "Мне кажется, что даже когда война закончится, даже если в РФ придёт новая власть и уйдёт пропаганда,\
                #     я уже никогда не буду чувствовать себя в полной безопасности."
                self.text_output.insert(END, t.translit_file_cy_lt(texte))
            # else:
            #     self.text_output.insert(END, "Your text is not in Russian")
        except Exception as e:
            messagebox.showerror(e)

    # Clearing text fields
    def clear(self):
        self.text_input.delete(1.0, END)
        self.text_output.delete(1.0, END)


app = Interface()
app.title("GUI for transliteration")
app.mainloop()
