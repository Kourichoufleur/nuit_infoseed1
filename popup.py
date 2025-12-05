import tkinter as tk

import tkinter as tk
from funcs import *

def desactiver_frame(frame):
    for child in frame.winfo_children():
        try:
            if isinstance(child, tk.Frame):
                desactiver_frame(child)
            else:
                child.config(state="disabled")
        except tk.TclError:
            pass  # certains widgets n'ont pas de state


def init(obj, taille_grille):
    for i in range(taille_grille):
        obj.columnconfigure(i, weight=1)
        obj.rowconfigure(i, weight=1)


import os
import sys
from PIL import Image, ImageTk

# cle : nom image / valeur : (display_name, catcha_info)

POP_UPS_INFO = {
    "boymoney": ("Vivez heureux, vivez riche", {}),
    "cake": ("Marie_clode vous a invité pour ses 92 ans !", {}),
    "catwall": ("Miaou adoptez moi", {}),
    "joyfulmeadow": ("Retrouvez votre enfance perdue...", {}),
    "omg": ("AAAAAAAAAAAAAAAA", {}),
    "playa": ("Vous avez gagné 2 mois de vacances!", {}),
    "scary": ("Prudence après minuit...", {}),
    "unseriousdog": ("Besoin d'un nouveau look ?", {}),
    "catsmugface": ("On sait qui vous êtes...", {}),
    "creepcameraman": ("J'ai besoin de ta tête !", {}),
    "disturbheart": ("Kristelle a publiée ceci sur votre mur", {}),
    "freecandy": ("Bonbons gratuits pour tous !", {}),
    "graduate": ("Je suis votre fils! graduation_info.com", {}),
    "oh": ("Bon courage", {}),
    "shibajujuding": ("Arrêtez de laisser les crottes au sol", {}),
    "sigma": ("Pratiquez votre mewing tous les jours !", {}),
    "tiredcat": ("Promo sur les vitamines C", {}),
    "troll": ("Trololololo", {}),
    "urfcat": ("112 messages non lus... nan mais serieux.", {}),
    "warning": ("2 virus et demi détectés !", {}),

}




couleurs_arc_en_ciel_et_plus = ["#FF0000", "#FFA500", "#FFFF00", "#00FF00", "#00FFFF", "#F7BDBD", "#8CFF39", "#EE82EE",
                                "#FF00FF", "#FFFFFF"]

import random


class Popup(tk.Toplevel):
    def __init__(self, parent, geometry="300x300", image=None, title="", color="grey", *args, **kwargs):
        super().__init__(parent)

        self.geometry(geometry)

        self.frame = tk.Frame(self)
        self.overrideredirect(True)
        self.attributes("-topmost", True)

        self.top_row = tk.Frame(self.frame)

        self.top_row.configure(background="gray")

        self.close_button = tk.Button(self.top_row, text="X", command=lambda: self.close())

        self.close_button.configure(background="red", foreground="white")
        self.close_button.pack(side="right", anchor="ne")

        self.title = tk.Label(self.top_row, text=title or "VOICI UN POPUP INUTILE", font=("Comic Sans MS", 10),
                              bg=random.choice(couleurs_arc_en_ciel_et_plus))
        self.title.pack(side="left", fill="x", expand=True)

        self.top_row.pack(side="top", fill="x", expand=True)

        self.image = image

        if self.image:
            self.label_image = tk.Label(self.frame, image=self.image)
            self.label_image.pack(side="bottom", fill="both", expand=True)

        self.frame.pack()

    def close(self):
        self.destroy()


def lancer_n_popup(frame, images=None, n=3, size=(300, 300)):
    if n <= 0: return
    import random
    if not images: images = load_images("popup_images", size=size)

    Popup(frame, image=(choosed := random.choice(images))[1], title=POP_UPS_INFO.get(choosed[0], ("",))[0],
          geometry=f"300x300+{random.randint(0, 1000)}+{random.randint(0, 1000)}")
    frame.after(100, lambda: lancer_n_popup(frame, images, n - 1))


if __name__ == "__main__":
    test = tk.Tk()

    test.withdraw()

    test.after(100, lambda: lancer_n_popup(test))
    test.mainloop()
