import tkinter as tk
import tkinter.ttk as ttk
class Clavier:
    def __init__(self, main_frame, textInput):
        self.main_frame = main_frame
        self.my_screen = tk.Toplevel(main_frame)

        self.my_screen.protocol("WM_DELETE_WINDOW", lambda: None)
        self.my_screen.geometry(f'1500x300+{int(main_frame.winfo_rootx())}+{int(main_frame.winfo_height()+main_frame.winfo_rooty())+150}')
        self.my_screen.resizable(False, False)
        self.my_screen.title('Clavier')
        self.text_input = textInput  # variable où tu injectes le caractère

        self.all_rows = []
        self.all_rows_panel = tk.Frame(self.my_screen)
        self.all_rows_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.selected_char = tk.StringVar()
        self.selected_char.set('')


        self.entrer_et_supp = tk.Frame(self.my_screen)
        self.entrer = ttk.Button(self.entrer_et_supp, text='Entrer caractère',
                                command=self.injecter_char)
        self.delete = ttk.Button(self.entrer_et_supp, text='Supprimer',
                                command=self.supprimer)
        self.entrer_et_supp.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.entrer.pack(side=tk.TOP, fill=tk.BOTH)
        self.delete.pack(side=tk.BOTTOM, fill=tk.BOTH)

        all_letter1 = "abcdefghijklmno"
        all_letter2 = "pqrstuvwxyzABCDE"
        all_letter3 = "FGHIJKLMNOP@.-_"
        all_letters = [all_letter1, all_letter2, all_letter3]

        for i in range(3):
            row = tk.Frame(self.all_rows_panel)
            row.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            for letter in all_letters[i]:   # <-- UN caractère à la fois
                b = ttk.Button(row, text=letter,
                              command=lambda c=letter: self.selected_char.set(c))
                b.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.all_rows.append(row)

    def injecter_char(self):
        # ajoute le caractère dans ta boîte de texte
        self.text_input.configure(state="normal")
        self.text_input.insert(tk.END, self.selected_char.get())
        self.text_input.configure(state="readonly")

    def supprimer(self):
        self.text_input.configure(state="normal")
        self.text_input.delete(0, tk.END)
        self.text_input.configure(state="readonly")
