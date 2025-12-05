import tkinter as tk
import tkinter.messagebox
import  tkinter.ttk as ttk
import constants
from clavier import Clavier
from funcs import *
from conte import*
from ohnoitgrowth import Growth
from register import Register
import tkinter.font as tkfont
from mailbox import*
toi=Register()



def envoyer(event=None):
    global email,clavier
    main.withdraw()
    toi.message=entry.get()
    desactiver_frame(root)
    entry.configure(state="readonly")
    tk.messagebox.showerror("Manque de compte", "Il vous faut un compte")
    email=Conte(root,"Saisissez votre email",email_envoie)
    clavier=Clavier(root,email.entry)

def email_envoie(event=None):
    global email,clavier,mot_de_passe
    clavier.my_screen.withdraw()
    toi.email=email.entry.get()
    email.my_screen.destroy()
    if(tk.messagebox.askyesno("MDP?","Voulez vous entrer votre mot de passe")) :
        mot_de_passe = Conte(root, "Saisissez votre mot de passe", envoie_mdp)
        clavier.my_screen.deiconify()
        clavier.text_input = mot_de_passe.entry

    else:
        tk.messagebox.showinfo("MDP!", "Ne vous inquétez pas nous avons récupéré votre dernier mot de passe utilisé")
        toi.password = "louvre"
        confirmation()
        clavier.my_screen.destroy()

def lancer (i):
    couleurs_arc_en_ciel_et_plus=["#FF0000","#FFA500","#FFFF00", "#00FF00", "#00FFFF","#0000FF","#4B0082", "#EE82EE","#FF00FF","#FFFFFF"]
    fenetre = Growth(root, max_taille=250, pas=5, delai=20, text=str(i),couleur=couleurs_arc_en_ciel_et_plus[10-i])
    fenetre.demarrer_croissance(delai_initial=100)

    if i==1: encour.set(False)

global i
i=10
def control_sequence():
    global i
    if i >= 1:
        lancer(i)
        i -= 1
        root.after(5000, control_sequence)
    else:
        root.destroy()
        main.deiconify()
        mailboxing=FakeMailReaderApp(main,toi)
def confirmation():
    if(tk.messagebox.askyesno("Email","Voulez vous que l'on vous envoie un email de confirmation ?")) :
        pass
    else:
        tk.messagebox.showinfo("En fait si","Si si on va le faire quand même")
    tk.messagebox.showwarning("a maince","il y a une demande aflluente de mail veuillez attendre")
    control_sequence()


def envoie_mdp(evevent=None):
    global mot_de_passe,clavier
    toi.password=mot_de_passe.entry.get()
    mot_de_passe.my_screen.destroy()
    clavier.my_screen.destroy()
    confirmation()
    print(toi.password + "   " + toi.email)

main = tk.Tk()
encour = tk.BooleanVar(value=True)
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