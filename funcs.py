import tkinter as tk
def desactiver_frame(frame):
    for child in frame.winfo_children():
        try:
            if isinstance(child, tk.Frame):
                desactiver_frame(child)
            else :
                child.config(state="disabled")
        except tk.TclError:
            pass  # certains widgets n'ont pas de state


def init(obj,taille_grille):
    for i in range(taille_grille):
        obj.columnconfigure(i, weight=1)
        obj.rowconfigure(i, weight=1)

import os
import sys
from PIL import Image, ImageTk

# --- CHEMIN DES RESSOURCES ---
def resource_path(relative_path):
    """Retourne le bon chemin, même dans le .exe"""
    try:
        base_path = sys._MEIPASS  # dossier temporaire PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# --- CHARGEMENT DES IMAGES POUR TKINTER ---
def load_images(folder, size=(300, 300)):
    images = []
    folder_path = resource_path(folder)
    if not os.path.exists(folder_path):
        print("⚠️ Dossier introuvable :", folder_path)
        return images

    for file in os.listdir(folder_path):
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
            name = os.path.splitext(file)[0]

            pil_img = Image.open(os.path.join(folder_path, file)).convert("RGBA")

            # Resize ici 🤌
            pil_img = pil_img.resize(size)

            tk_img = ImageTk.PhotoImage(pil_img)

            images.append((name, tk_img))

    return images
