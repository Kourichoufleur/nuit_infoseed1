from tkinter import *
from time import sleep

import tkinter as tk
from tkinter import ttk
import time


class Growth:
    def __init__(self, master, max_taille=2000, pas=5, delai=10,text=None,couleur="white"):

        # Création de la fenêtre de niveau supérieur
        self.a = tk.Toplevel(master)
        self.a.title("Oh no it growth")


        self.a.protocol("WM_DELETE_WINDOW", lambda: None)


        self.a.geometry("0x0+0+0")


        self.a.overrideredirect(True)
        self.a.configure(background=couleur)
        self.a.attributes("-topmost", True)
        self.a.grid_rowconfigure(0, weight=1)
        self.a.grid_columnconfigure(0, weight=1)

        self.label=tk.Label(self.a, text=text, font=("Arial", 0),background=couleur,padx=5,pady=5)
        self.label.grid(row=0, column=0, sticky=tk.NSEW)

        # Paramètres de croissance
        self.max_taille = max_taille
        self.pas = pas
        self.delai = delai
        self.compteur = 0

    def grandir(self):
        if self.compteur < self.max_taille:

            # Calculer les nouvelles dimensions
            nouvelle_largeur = self.a.winfo_width() + self.pas
            nouvelle_hauteur = self.a.winfo_height() + self.pas

            # Appliquer la nouvelle géométrie
            self.a.geometry(f"{nouvelle_largeur}x{nouvelle_hauteur}+0+0")

            self.compteur += 1

            # Appeler la fonction à nouveau après un délai
            self.a.after(self.delai, self.grandir)
            self.label.configure(font=("Arial",int(nouvelle_largeur /2 )),padx=10,pady=10)
        else:
            self.a.destroy()

    def demarrer_croissance(self, delai_initial=100):
        """
        Démarre le processus de croissance après un délai initial.
        """
        self.a.after(delai_initial, self.grandir)

def genlancer(i):
    return lambda :lancer(i)
def lancer (i):
    couleurs_arc_en_ciel_et_plus=["#FF0000","#FFA500","#FFFF00", "#00FF00", "#00FFFF","#0000FF","#4B0082", "#EE82EE","#FF00FF","#FFFFFF"]
    fenetre = Growth(root, max_taille=300, pas=5, delai=30, text=str(i),couleur=couleurs_arc_en_ciel_et_plus[10-i])
    fenetre.demarrer_croissance(delai_initial=100)
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Fenêtre Principale Invisible")

    # Cache la fenêtre root car elle n'est pas nécessaire pour cet effet
    root.withdraw()

    # 1. Créer une instance de la classe
    # (max_taille réduit à 500 pour un test plus rapide)

    root.deiconify()


    # 2. Démarrer l'animation


    root.mainloop()

