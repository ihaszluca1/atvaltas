from tkinter import *

# Ablak létrehozása
root = Tk()
root.title("Átváltó")
root.config(bg="#cce3de")

hossz_button = Button(root, text="Hosszúság átváltás", bg="#a4c3b2", font=("Arial", 12))
hossz_button.grid(column=0, row=6, padx=5, pady=10)

# Futtatás
root.mainloop()