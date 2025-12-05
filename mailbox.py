import tkinter as tk
from tkinter import ttk, scrolledtext
from messages import MESSAGES
# --- 1. Les Données Statiques (Vos Faux Messages) ---
# Chaque clé est l'identifiant unique du message.
# Chaque valeur contient un dictionnaire avec les détails.



# --- 2. Fonctions de l'Interface Graphique ---

class FakeMailReaderApp:
    def __init__(self, master):
        self.master = master
        master.title("Boîte de Réception Statique (Tkinter)")

        # Configuration des styles
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')

        # --- Cadre Principal ---
        main_frame = ttk.Frame(master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- 1. Liste des Messages (Partie Gauche) ---
        list_frame = ttk.Frame(main_frame, width=400, height=500)
        list_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        list_frame.pack_propagate(False)

        ttk.Label(list_frame, text="Messages Statiques:", font=('Helvetica', 10, 'bold')).pack(pady=(0, 5))

        # Le Listbox stocke les titres visibles
        self.messages_listbox = tk.Listbox(list_frame, width=60, height=25, font=('Courier', 10))
        self.messages_listbox.pack(fill=tk.BOTH, expand=True)
        # On lie la sélection à la fonction d'affichage
        self.messages_listbox.bind('<<ListboxSelect>>', self.on_message_select)

        # Stocker les clés des messages (MSG_001, MSG_002, ...) pour référence facile
        self.message_keys = []
        self.load_fake_emails()

        # --- 2. Contenu du Message (Partie Droite) ---
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.header_label = ttk.Label(content_frame, text="Sélectionnez un message.", font=('Helvetica', 10, 'italic'))
        self.header_label.pack(fill=tk.X, pady=(0, 5))

        self.message_content_area = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=80, height=30,
                                                              font=('Courier', 10))
        self.message_content_area.pack(fill=tk.BOTH, expand=True)
        self.message_content_area.insert(tk.END, "Le contenu du message sélectionné apparaîtra ici.")
        self.message_content_area.config(state=tk.DISABLED)  # Rendre non éditable

    def load_fake_emails(self):
        """Charge les messages statiques dans le Listbox."""
        self.messages_listbox.delete(0, tk.END)
        self.message_keys = []

        for key, data in MESSAGES.items():
            self.message_keys.append(key)
            self.messages_listbox.insert(tk.END, data["titre_liste"])

    def on_message_select(self, event):
        """Affiche le contenu du message sélectionné."""

        if not self.messages_listbox.curselection():
            return

        selected_index = self.messages_listbox.curselection()[0]
        # Récupère la clé unique (ex: "MSG_001") correspondant à l'index sélectionné
        message_key = self.message_keys[selected_index]
        message_data = MESSAGES[message_key]

        # 1. Mise à jour de l'en-tête
        self.header_label.config(text=f"De: {message_data['expediteur']}")

        # 2. Affichage du corps du message
        self.message_content_area.config(state=tk.NORMAL)
        self.message_content_area.delete(1.0, tk.END)
        self.message_content_area.insert(tk.END, message_data["corps"])
        self.message_content_area.config(state=tk.DISABLED)


# --- 3. Exécution de l'Application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = FakeMailReaderApp(root)
    root.mainloop()