import tkinter as tk

import tkinter as tk
from funcs import *
from screeninfo import get_monitors

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
    "boymoney": ("Vivez heureux, vivez riche", {"charisme":6, "maman":8}),
    "cake": ("Marie_clode vous a invité pour ses 92 ans !", {"charisme":2, "maman":10}),
    "catwall": ("Miaou adoptez moi", {"charisme":3, "maman":7, "chat":True}),
    "joyfulmeadow": ("Retrouvez votre enfance perdue...", {"charisme":2, "maman":8}),
    "omg": ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", {"charisme":5, "maman":9}),
    "playa": ("Vous avez gagné 2 mois de vacances!", {"charisme":2, "maman":8}),
    "scary": ("Prudence après minuit...", {"charisme":8, "maman":1}),
    "unseriousdog": ("Besoin d'un nouveau look ?", {"charisme":6, "maman":10}),
    "catsmugface": ("On sait qui vous êtes...", {"charisme":10, "maman":3, "chat":True}),
    "creepcameraman": ("J'ai besoin de ta tête !", {"charisme":0, "maman":0}),
    "disturbheart": ("Kristelle a publiée ceci sur votre mur", {"charisme":4, "maman":10}),
    "freecandy": ("Bonbons gratuits pour tous !", {"charisme":0, "maman":0}),
    "graduate": ("Je suis votre fils! graduation_info.com", {"charisme":6, "maman":10}),
    "oh": ("Bon courage", {"charisme":1, "maman":2}),
    "shibajujudging": ("Arrêtez de laisser les crottes au sol", {"charisme":7, "maman":7}),
    "sigma": ("Pratiquez votre mewing tous les jours !", {"charisme":10, "maman":5}),
    "tiredcat": ("Promo sur les vitamines C", {"charisme":3, "maman":5, "chat":True}),
    "troll": ("Trololololo", {"charisme":0, "maman":1}),
    "urfcat": ("112 messages non lus... nan mais serieux.", {"charisme":0, "maman":2, "chat":True}),
    "warning": ("2 virus et demi détectés !", {"charisme":1, "maman":1}),
    "classemoji":("Soyez cool dans la vie...",{"charisme":9, "maman":3}),

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


def lancer_n_popup(frame, images=None, n=30, size=(300, 300)):
    if n <= 0: return
    import random
    if not images: images = load_images("popup_images", size=size)

    ecran_princ = get_monitors()[0]
    Popup(frame, image=(choosed := random.choice(images))[1], title=POP_UPS_INFO.get(choosed[0], ("",))[0],
          geometry=f"300x300+{random.randint(0, abs(ecran_princ.width - 300))}+{random.randint(0, abs(ecran_princ.height - 300))}")
    frame.after(100, lambda: lancer_n_popup(frame, images, n - 1))


if __name__ == "__main__":
    test = tk.Tk()

    test.withdraw()

    test.after(100, lambda: lancer_n_popup(test))
    test.mainloop()
