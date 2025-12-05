import random
import tkinter as tk
from tkinter import messagebox
from funcs import load_images
from popup import POP_UPS_INFO

# --- Statistiques ---
all_stat = (
    ("charisme", True),
    ("chat", False),
    ("maman", True),
)
dict_stat = dict(all_stat)  # clé -> bool (True = numérique, False = booléen)

STATS_DESC = {
    "charisme": ("Veuillez sélectionner les images ayant au moins", "sur 10 de charisme"),
    "chat": ("Veuillez sélectionner les images étant des chats", ""),
    "maman": ("Veuillez sélectionner les images ayant au moins", "chance sur 10 d'être aimé par votre maman"),
}

class Capchat(tk.Toplevel):
    def __init__(self, master, property_used="charisme", seuil=1,fun=lambda:...,truc=None):
        super().__init__(master)
        self.fun=fun
        self.resizable(False, False)
        self.withdraw()


       

        # --- Consigne ---
        desc = STATS_DESC[property_used]
        consigne_text = desc[0]
        if dict_stat[property_used]:  # si c'est une stat numérique
            consigne_text += f" {seuil} {desc[1]}"
        self.consigne = tk.Label(self, text=consigne_text, font=("Arial", 12), pady=10)
        self.consigne.pack(side="top", fill="x")
        self.transient(master)
        self.lift(master)
        # --- Centrer la fenêtre ---
        self.update_idletasks()
        width, height = 650, 650
        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        # --- Frame pour les images ---
        self.images_frame = tk.Frame(self)
        self.images_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- Charger les images ---
        all_images = load_images("popup_images", (200,200))
        if len(all_images) < 9:
            messagebox.showerror("Erreur", "Pas assez d'images pour générer le captcha !")
            self.destroy()
            return

        used = random.sample(all_images, 9)

        self.all_b = {}          # pour stocker les boutons
        self.images_refs = []    # garder les images en mémoire
        self.to_demask = 0       # compteur des bonnes images

        # --- Créer la grille 3x3 ---
        for i in range(3):
            self.images_frame.columnconfigure(i, weight=1)
            self.images_frame.rowconfigure(i, weight=1)
            for j in range(3):
                img_name, img = used[i*3+j]
                self.images_refs.append(img)

                # --- Vérification si image valide ---
                entry = POP_UPS_INFO.get(img_name, (None, {}))
                prop_dict = entry[1] if len(entry) > 1 else {}

                if dict_stat[property_used]:  # numérique
                    print(f"Le bouton a l'indice {(i,j)} a la stat a {prop_dict.get(property_used, 0)} et le seuil est à {seuil}")
                    is_valid = prop_dict.get(property_used, 0) >= seuil
                else:  # booléen
                    is_valid = bool(prop_dict.get(property_used, 0))

                if is_valid:
                    self.to_demask += 1

                # --- Bouton avec capture safe ---
                btn = tk.Button(
                    self.images_frame,
                    image=img,
                    command=lambda valid=is_valid, coords=(i,j): self.test(valid, coords)
                )
                btn.grid(column=i, row=j, sticky="nsew", padx=2, pady=2)
                self.all_b[(i,j)] = btn
        
        self.transient(master)
        self.lift()
        self.deiconify()
        self.title("Super Capcha-t")
        self.geometry("650x650")

    # --- Fonction test ---
    def test(self, is_valid, coords):
        button = self.all_b.get(coords)
        if is_valid:
            self.to_demask -= 1
            if button:
                button.configure(state=tk.DISABLED, image=None, bg="blue")
            if self.to_demask == 0:
                messagebox.showinfo("Succès", "Bravo ! Vous avez réussi le captcha 🎉")
                self.withdraw()
                self.fun()
                self.destroy()

        else:
            messagebox.showwarning(
                "Attention",
                "Vous vous êtes trompé. Veuillez réessayer !"
            )
            self.destroy()
            # --- Relancer un nouveau captcha proprement ---
            new_stat, is_numeric = random.choice(all_stat)
            new_seuil = random.randint(1,10) if is_numeric else 0
            Capchat(self.master, new_stat, new_seuil, self.fun)

# --- Test ---
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # cacher la fenêtre principale
    new_stat, is_numeric = random.choice(all_stat)
    new_seuil = random.randint(1, 10) if is_numeric else 0
    Capchat(root, new_stat, new_seuil)
    root.mainloop()
