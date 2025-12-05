import tkinter as tk
import webbrowser
from random import randint
from tkinter import ttk, scrolledtext

from capchat import Capchat, all_stat
from messages import MESSAGES
import magique as mg
from popup import *
class FakeMailReaderApp:
    def __init__(self, master,toi):
        self.toi=toi
        self.master = master
        master.title("Boîte de Réception Statique (Tkinter)")

        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')

        # --- Cadre Principal ---
        self.main_frame = ttk.Frame(master, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # --- 1. Liste des Messages (Partie Gauche) ---
        list_frame = ttk.Frame(self.main_frame, width=400, height=500)
        list_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        list_frame.pack_propagate(False)

        ttk.Label(list_frame, text="Messages Statiques:", font=('Helvetica', 10, 'bold')).pack(pady=(0, 5))

        self.messages_listbox = tk.Listbox(list_frame, width=60, height=25, font=('Courier', 10))
        self.messages_listbox.pack(fill=tk.BOTH, expand=True)
        self.messages_listbox.bind('<<ListboxSelect>>', self.on_message_select)

        self.message_keys = []
        self.load_fake_emails()

        # --- 2. Contenu du Message (Partie Droite) ---
        content_frame = ttk.Frame(self.main_frame)
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.header_label = ttk.Label(content_frame, text="Sélectionnez un message.", font=('Helvetica', 10, 'italic'))
        self.header_label.pack(fill=tk.X, pady=(0, 5))

        self.message_content_area = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=80, height=30,
                                                              font=('Courier', 10))
        self.message_content_area.pack(fill=tk.BOTH, expand=True)
        self.message_content_area.insert(tk.END, "Le contenu du message sélectionné apparaîtra ici.")
        self.message_content_area.config(state=tk.DISABLED)

        # --- 3. Définition des Tags pour le Lien Cliquable ---
        self.message_content_area.tag_config('clickable_link',
                                             foreground='blue',
                                             underline=True)
        # Lier l'événement de clic à la fonction de lancement du toplevel
        self.message_content_area.tag_bind('clickable_link',
                                           '<Button-1>',  # Clic gauche de la souris
                                           self.launch_toplevel)

    def load_fake_emails(self):
        """Charge les messages statiques dans le Listbox."""
        self.messages_listbox.delete(0, tk.END)
        self.message_keys = []

        for key, data in MESSAGES.items():
            self.message_keys.append(key)
            self.messages_listbox.insert(tk.END, data["titre_liste"])

    def on_message_select(self, event):
        """Affiche le contenu du message sélectionné et applique le tag de lien."""

        if not self.messages_listbox.curselection():
            return

        selected_index = self.messages_listbox.curselection()[0]
        message_key = self.message_keys[selected_index]
        message_data = MESSAGES[message_key]
        if (message_key!="MSG_004"):
            lancer_n_popup(self.main_frame,n=randint(3,7))

        # 1. Mise à jour de l'en-tête
        self.header_label.config(text=f"De: {message_data['expediteur']}")

        # 2. Affichage du corps du message
        self.message_content_area.config(state=tk.NORMAL)
        self.message_content_area.delete(1.0, tk.END)
        self.message_content_area.insert(tk.END, message_data["corps"])

        # 3. Rendre le lien cliquable si un lien est défini pour ce message
        if message_data.get("lien_texte"):
            lien_texte = message_data.get("lien_texte")

            # Utilise 'search' pour trouver la position du texte du lien
            start_pos = '1.0'
            while True:
                # Cherche la prochaine occurrence du texte du lien
                start_index = self.message_content_area.search(lien_texte, start_pos, stopindex=tk.END)

                if not start_index:
                    break

                # Calcule l'index de fin (index de départ + longueur du texte)
                end_index = f"{start_index}+{len(lien_texte)}c"

                # Applique le tag 'clickable_link' à cette plage de texte
                self.message_content_area.tag_add('clickable_link', start_index, end_index)

                # Prépare la recherche pour la prochaine occurrence après la fin de celle-ci
                start_pos = end_index

        self.message_content_area.config(state=tk.DISABLED)

    # --- Nouvelle Fonction pour le Toplevel ---
    def launch_toplevel(self, event):
        self.master.withdraw()
        new_stat, is_numeric = random.choice(all_stat)
        new_seuil = random.randint(1, 10) if is_numeric else 0
        Capchat(self.master, new_stat, new_seuil,fun=self.fun)

          # Nécessaire pour empêcher la sélection de texte du lien
        return "break"

    def fun(self):
        self.master.deiconify()
        toplevel = tk.Toplevel(self.master)
        toplevel.title("Détails du Lien (Toplevel)")
        toplevel.geometry("600x300")
        self.master.withdraw()

        def ouvrir_lien(event=None):
            """Ouvre l'URL spécifiée dans le navigateur web par défaut."""
            try:
                webbrowser.open_new("https://nird.forge.apps.education.fr")
            except Exception:
                pass

        def creer_hyperlien(parent, texte):
            """Crée un Label qui se comporte comme un lien hypertexte."""

            # Création du Label
            label = tk.Label(parent, text=texte,
                             fg="blue",
                             cursor="hand2",  # Curseur en forme de main au survol
                             font=('Arial', 10, 'underline'))  # Police soulignée

            label.bind("<Button-1>", ouvrir_lien)

            def on_enter(event):
                label.config(fg="red")  # Change la couleur en rouge au survol

            def on_leave(event):
                label.config(fg="blue")  # Retourne au bleu quand la souris quitte

            label.bind("<Enter>", on_enter)
            label.bind("<Leave>", on_leave)

            return label

        ttk.Label(toplevel,
                  text="Trop de contrainte  de création de compte\n inutile partout mais NIRD recycle les appareils \n"
                       + "usagées et enleve toute ses conexions intulies", font=('Helvetica', 12, 'bold')).pack(
            pady=10, padx=10)
        hyperlien = creer_hyperlien(toplevel, "Site de NIRD", )
        hyperlien.pack(pady=20, padx=20)

        def truc():
            self.main_frame.destroy()
            toplevel.destroy()
            magique = mg.AnimatedApp(self.master, self.toi.message)

        ttk.Button(toplevel, text="obtenir votre texte magique", command=truc).pack(pady=10)



# --- 4. Exécution de l'Application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = FakeMailReaderApp(root,None)
    root.mainloop()
