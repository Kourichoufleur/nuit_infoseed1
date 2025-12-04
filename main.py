import tkinter as tk
import tkinter.messagebox
import  tkinter.ttk as ttk
import constants
from clavier import Clavier
from funcs import *
from conte import*
from register import Register
toi=Register()

def envoyer(event=None):
    global email,clavier
    desactiver_frame(root)
    entry.configure(state="readonly")
    tk.messagebox.showerror("Manque de compte", "Il vous faut un compte")
    email=Conte(root,"Saisissez votre email",email_envoie)
    clavier=Clavier(root,email.entry)

def email_envoie(event=None):
    global email,clavier,mot_de_passe
    toi.email=email.entry.get()
    email.my_screen.destroy()
    if(tk.messagebox.askyesno("Il vous faut","Voulez vous entrer votre mot de passe")) :
        mot_de_passe = Conte(root, "Saisissez votre mot de passe", envoie_mdp)
        clavier.text_input = mot_de_passe.entry

    else:
        tk.messagebox.showinfo("Il vous faut", "Ne vous inquétez pas nous avons récupéré votre dernier mot de passe utilisé")
        toi.password = "louvre"
        print(toi.password + "   " + toi.email)

    # vider l'entry
def envoie_mdp(evevent=None):
    global mot_de_passe,clavier
    toi.password=mot_de_passe.entry.get()
    mot_de_passe.my_screen.destroy()
    print(toi.password + "   " + toi.email)

main = tk.Tk()
main.title("Chat Entry")
root= tk.Frame(main)
root.configure(relief="groove")
root.configure(cursor="arrow")
root.pack(fill="both",expand=True)

init(root,constants.TAILLE_GRILLE)


instructions=tk.Label(root,text="Entrez votre text pour le rendre magique",font=("Arial",30))
instructions.grid(row=0, column=0, padx=10, pady=10,sticky="new")

entry_frame = tk.Frame(root)
entry_frame.grid(row=1, column=0, padx=10, pady=10,sticky="news")
init(entry_frame,3)

envoie=ttk.Button(entry_frame,text="Envoyer",command=envoyer,)
envoie.grid(row=1, column=2, padx=0, pady=10,sticky="news")

entry = tk.Entry(entry_frame, font=("Arial", 16))
entry.grid(row=1, column=0, sticky="news", padx=0, pady=10,columnspan=2)


main.mainloop()