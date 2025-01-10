from tkinter import *

# Ablak létrehozása
root = Tk()
root.title("Átváltó")
root.config(bg="#a3cef1")



def hossz():
    def show(): 
        eredm.config(text = clicked.get())
    
    top = Toplevel()
    top.title("Hosszúság átváltás")
    top.config(bg="#a3cef1")

    entry = Entry(top, width=20, font=("Arial", 15), borderwidth=1, relief="solid", justify="center")
    entry.grid(column=0, row=1, columnspan=2, padx=3, pady=5)

    options = ["milliméter", "centiméter", "deciméter", "méter", "kilométer"]
    clicked = StringVar()
    clicked.set( "méter")
    drop = OptionMenu(top , clicked , *options)
    drop.grid(column=2, row=1, padx=5, pady=10)

    szamol_button = Button(top, text="Számol", bg="#0d3b66", font=("Arial", 12), fg="white", command=show)
    szamol_button.grid(column=0, row=3, padx=3, pady=5)

    back_button = Button(top, text="Bezár", bg="#0d3b66", font=("Arial", 12), fg="white", command=top.destroy)
    back_button.grid(column=1, row=3, padx=3, pady=5)

    eredm = Label(top, text="", font=("Arial", 20), bg="#a3cef1")
    eredm.grid(column=0, row=2, columnspan=2, pady=10)



def tomeg():
    top = Toplevel()



def urmerek():
    top = Toplevel()







label_szoveg = Label(root, text="Válaszd ki mit szeretnél átváltatni!", font=("Arial", 20), bg="#a3cef1")
label_szoveg.grid(column=0, row=1, columnspan=2, pady=10)

hossz_button = Button(root, text="Hosszúság átváltás", bg="#0d3b66", font=("Arial", 12), fg="white", command=hossz)
hossz_button.grid(column=0, row=2, padx=5, pady=10)

tomeg_button = Button(root, text="Tömeg átváltás", bg="#0d3b66", font=("Arial", 12), fg="white", command=tomeg)
tomeg_button.grid(column=1, row=2, padx=5, pady=10)

urmertek_button = Button(root, text="Űrmérték átváltás", bg="#0d3b66", font=("Arial", 12), fg="white", command=urmerek)
urmertek_button.grid(column=2, row=2, padx=5, pady=10)

stop_button = Button(root, text="Kilépés", bg="#0d3b66", font=("Arial", 12), fg="white")
stop_button.grid(column=1, row=3, padx=5, pady=10)




# Futtatás
root.mainloop()