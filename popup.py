import tkinter as tk
from funcs import *



class Popup(tk.Toplevel):
    def __init__(self, parent, geometry="300x300", image=None, *args, **kwargs):
        super().__init__(parent)

        self.geometry(kwargs.get("geometry","300x300"))
        self.image = image

        self.frame = tk.Frame(self)
        self.overrideredirect(True)

        self.top_row = tk.Frame(self.frame)

        self.top_row.configure(background="gray")

        self.close_button = tk.Button(self.top_row,text="X", command=lambda : self.close())

        self.close_button.configure(background="red", foreground="white")
        self.close_button.pack(side="right",  anchor="ne")

        self.top_row.pack(side="top", fill="x", expand=True)

        self.frame.pack()

    def close(self):
        self.destroy()


if __name__=="__main__":
    test = tk.Tk()

    images_popup = load_images("popup_images")


    Popup(test)
    test.mainloop()






