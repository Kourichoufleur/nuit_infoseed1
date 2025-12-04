import tkinter as tk
from funcs import*
import tkinter.ttk as ttk
class Conte:
    def __init__(self, main_frame,text,envoyer):

        self.main_frame = main_frame
        self.my_screen = tk.Toplevel(main_frame)

        self.my_screen.protocol("WM_DELETE_WINDOW", lambda: None)

        self.my_screen.geometry('800x300')
        self.my_screen.resizable(False, False)
        self.my_screen.title('Creation de conte')

        self.label=tk.Label(self.my_screen, text=text, font=("Arial", 30))
        self.label.grid(row=0, column=0, padx=10, pady=10,sticky="new")
        self.frame=tk.Frame(self.my_screen)
        self.frame.grid(row=1, column=0, padx=10, pady=10,sticky="new")
        init(self.frame, 3)

        self.envoie = ttk.Button(self.frame, text="Envoyer", command=envoyer )
        self.envoie.grid(row=1, column=2, padx=0, pady=10, sticky="news")

        self.entry = tk.Entry(self.frame, font=("Arial", 16))
        self.entry.grid(row=1, column=0, sticky="news", padx=0, pady=10, columnspan=2)
        self.entry.configure(state="readonly")
    def injecter_char(self):
        # ajoute le caractère dans ta boîte de texte
        self.text_input.insert(tk.END, self.selected_char.get())

    def supprimer(self):
        self.text_input.delete(0, tk.END)
