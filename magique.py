import tkinter as tk
import random
import math

# --- Configuration de l'Animation ---
LARGEUR = 800
HAUTEUR = 600
TEXTE_COULEUR = "#FFFFFF"  # Blanc

# --- Paramètres des Particules (Feux d'Artifice/Étoiles) ---
NB_PARTICULES = 100
PARTICULES = []

# --- Paramètres de l'Effet de Couleur de Fond ---
COULEUR_INITIALE = (0, 0, 0)  # Noir
VITESSE_COULEUR = 1.0  # Vitesse de changement
COULEUR_ACTUELLE = list(COULEUR_INITIALE)


class AnimatedApp:
    def __init__(self, master,message):
        self.text_animation=message
        self.master = master
        master.title("🎉 Votre récompense 🎆")
        self.rotation_angle = 0

        self.canvas = tk.Canvas(master, width=LARGEUR, height=HAUTEUR, bg='#000000')
        self.canvas.pack()

        # Initialisation du texte "3D"
        self.text_id = self.canvas.create_text(
            LARGEUR // 2, HAUTEUR // 2,
            text=self.text_animation,
            fill=TEXTE_COULEUR,
            font=('Impact', 72, 'bold')  # Utilisez une police percutante
        )
        # Création d'une ombre (pour l'effet 3D)
        self.shadow_id = self.canvas.create_text(
            LARGEUR // 2 + 3, HAUTEUR // 2 + 3,
            text=self.text_animation,
            fill='#333333',
            font=('Impact', 72, 'bold')
        )

        # Initialisation des particules
        self.init_particles()


        # Démarrage de la boucle d'animation
        self.animate_frame()

    # --- Gestion des Couleurs (Effet Hypnotisant) ---
    def update_background_color(self):

        global COULEUR_ACTUELLE

        # Fait varier la première composante de couleur (Rouge)
        COULEUR_ACTUELLE[0] += VITESSE_COULEUR
        if COULEUR_ACTUELLE[0] > 255:
            COULEUR_ACTUELLE[0] = 0
            # Quand le rouge est terminé, on passe à la composante suivante (Vert)
            COULEUR_ACTUELLE[1] += VITESSE_COULEUR * 2  # Change plus vite le Vert
            if COULEUR_ACTUELLE[1] > 255:
                COULEUR_ACTUELLE[1] = 0
                # Quand le vert est terminé, on passe au Bleu
                COULEUR_ACTUELLE[2] += VITESSE_COULEUR * 3  # Change encore plus vite le Bleu
                if COULEUR_ACTUELLE[2] > 255:
                    COULEUR_ACTUELLE[2] = 0  # Retour au début

        # Assurez-vous que les valeurs sont dans la plage [0, 255]
        r = int(min(255, max(0, COULEUR_ACTUELLE[0])))
        g = int(min(255, max(0, COULEUR_ACTUELLE[1])))
        b = int(min(255, max(0, COULEUR_ACTUELLE[2])))

        # Convertit RGB en couleur hexadécimale
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        self.canvas.config(bg=hex_color)

    # --- Gestion du Texte 3D (Flottement et Zoom) ---
    def update_text_animation(self, frame_count):
        """Ajoute un effet de rotation, de flottement et de pulsation (simulant l'axe Z) au texte."""

        # 1. Mise à jour de l'Angle de Rotation
        self.rotation_angle += 1.0 # Vitesse de rotation (1 degré par frame)
        if self.rotation_angle > 360:
            self.rotation_angle = 0

        # Effet de flottement vertical (sinusoidal)
        offset_y = 5 * math.sin(frame_count / 20.0)

        # Effet "3D" simple de perspective (mouvement léger de l'ombre)
        offset_shadow_x = 3 + 1 * math.cos(frame_count / 15.0)
        offset_shadow_y = 3 + 1 * math.sin(frame_count / 18.0)

        centre_x, centre_y = LARGEUR // 2, HAUTEUR // 2

        # --- NOUVEAU : Calcul de la Taille de Police (Effet Axe Z) ---
        taille_base = 72
        # Utilise cosinus pour une variation entre -1 et 1
        zoom_factor = 10 * math.cos(frame_count / 10.0)
        nouvelle_taille = int(taille_base + zoom_factor)

        # Assurer une taille minimale (pour ne pas disparaître)
        if nouvelle_taille < 60:
            nouvelle_taille = 60

        font_style = ('Impact', nouvelle_taille, 'bold')

        # --- APPLICATION DE LA ROTATION ET DU ZOOM ---

        # Suppression de l'ancien texte et de l'ombre
        self.canvas.delete(self.text_id)
        self.canvas.delete(self.shadow_id)

        # Recréation de l'ombre avec le nouvel angle et la nouvelle taille
        self.shadow_id = self.canvas.create_text(
            centre_x + offset_shadow_x, centre_y + offset_shadow_y + offset_y,
            text=self.text_animation,
            fill='#333333',
            font=font_style, # Utilisation de la nouvelle taille
            angle=self.rotation_angle
        )

        # Recréation du texte principal avec le nouvel angle et la nouvelle taille
        self.text_id = self.canvas.create_text(
            centre_x, centre_y + offset_y,
            text=self.text_animation,
            fill=TEXTE_COULEUR,
            font=font_style, # Utilisation de la nouvelle taille
            angle=self.rotation_angle
        )

        # Changement de couleur du texte pour un effet stroboscopique
        if frame_count % 10 < 5:
             self.canvas.itemconfig(self.text_id, fill="#FF00FF") # Magenta
        else:
             self.canvas.itemconfig(self.text_id, fill=TEXTE_COULEUR) # Blanc
    # --- Gestion des Particules (Feux d'Artifice) ---
    def init_particles(self):
        """Crée les données initiales pour toutes les particules."""
        for _ in range(NB_PARTICULES):
            # Position initiale aléatoire
            x = random.randint(0, LARGEUR)
            y = random.randint(0, HAUTEUR)
            # Vitesse et direction aléatoires (pour simuler une petite explosion)
            vx = random.uniform(-1.5, 1.5)
            vy = random.uniform(-1.5, 1.5)
            # Couleur aléatoire
            color = f'#{random.randint(0, 0xFFFFFF):06x}'

            # Créer l'objet graphique sur le canvas
            particle_id = self.canvas.create_oval(x, y, x + 5, y + 5, fill=color, outline=color)

            PARTICULES.append({
                'id': particle_id,
                'x': x,
                'y': y,
                'vx': vx,
                'vy': vy,
                'age': 0,
                'max_age': random.randint(50, 150)  # Durée de vie
            })

    def update_particles(self):
        """Met à jour la position, la gravité et recrée les particules."""

        new_particles = []
        for p in PARTICULES:
            # 1. Mise à jour de la position
            p['x'] += p['vx']
            p['y'] += p['vy']

            # 2. Application de la "gravité" légère
            p['vy'] += 0.05

            # 3. Vieillissement et dissipation (opacité ou taille)
            p['age'] += 1

            # 4. Vérification de la fin de vie
            if p['age'] < p['max_age'] and 0 < p['x'] < LARGEUR and 0 < p['y'] < HAUTEUR:
                # Si la particule est toujours "vivante"
                self.canvas.coords(p['id'], p['x'], p['y'], p['x'] + 3, p['y'] + 3)  # Diminution de la taille
                new_particles.append(p)
            else:
                # Si la particule doit "mourir", on la supprime du canvas
                self.canvas.delete(p['id'])
                # Et on en recrée une nouvelle immédiatement pour un flux constant
                self.spawn_new_particle()

        PARTICULES[:] = new_particles

    def spawn_new_particle(self):
        """Crée une nouvelle particule à un endroit aléatoire (simule une nouvelle explosion)."""
        x = random.randint(0, LARGEUR)
        y = random.randint(0, HAUTEUR)
        vx = random.uniform(-2, 2)
        vy = random.uniform(-2, 2)
        color = f'#{random.randint(0, 0xFFFFFF):06x}'

        particle_id = self.canvas.create_oval(x, y, x + 5, y + 5, fill=color, outline=color)

        PARTICULES.append({
            'id': particle_id,
            'x': x,
            'y': y,
            'vx': vx,
            'vy': vy,
            'age': 0,
            'max_age': random.randint(50, 150)
        })

    # --- Boucle Principale d'Animation ---
    def animate_frame(self):
        """Fonction appelée 60 fois par seconde pour mettre à jour l'état."""

        # Compteur pour la variation sinusoïdale (flottement)
        self.frame_count = getattr(self, 'frame_count', 0) + 1

        # 1. Mise à jour du fond
        self.update_background_color()

        # 2. Mise à jour du texte 3D
        self.update_text_animation(self.frame_count)

        # 3. Mise à jour des particules
        self.update_particles()

        # Planifie le prochain rafraîchissement (environ 60 images par seconde)
        self.master.after(16, self.animate_frame)

    # --- Exécution de l'Application ---


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedApp(root,"bite")
    root.mainloop()