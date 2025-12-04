from tkinter import *
from time import sleep


a = Tk()
a.title("Oh no it growth")

a.protocol("WM_DELETE_WINDOW", lambda: None)

a.geometry("0x0+0+0")
a.overrideredirect(True)
a.attributes("-topmost", True)

def grandir(i=0) :
    if i<2000 :
        a.geometry(f"{int(a.winfo_width())+5}x{int(a.winfo_height())+5}+0+0")
        a.after(10, lambda : grandir(i+1))
    else :
        a.destroy()

a.after(100,grandir)
a.mainloop()