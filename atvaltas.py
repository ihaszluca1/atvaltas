#Kötelező elemek importálása
from tkinter import *

# Ablak létrehozása és elnevezése
root = Tk()
root.title("Átváltó")
root.config(bg="#a3cef1")

#általános számolás
def convert(ertek, mibol, mibe, atvaltas_ertek):
    try:
        mibol1 = atvaltas_ertek[mibol]
        mibe1 = atvaltas_ertek[mibe]
        result = ertek * (mibol1 / mibe1)
        return result
    except KeyError:
        return "Érvénytelen mértékegység"


#hosszúság ablak létrehozása
def hossz():
    #mértékegységek érték adása
    def show(): 
        ertek = float(entry.get())  
        mibol = clicked_from.get()  
        mibe = clicked_to.get()  
        atvaltas_ertek = {
            "Milliméter": 1,
            "Centiméter": 10,
            "Deciméter": 100,
            "Méter": 1000,
            "Kilométer": 1000000
        }
        result = convert(ertek, mibol, mibe, atvaltas_ertek)
        eredm.config(text=f"Eredmény: {result} {mibe}")

    #hosszúság ablak elemeinek létrehozása, elrendezése, dizájnolása
    top = Toplevel()
    top.title("Hosszúság átváltás")
    top.config(bg="#a3cef1")

    entry = Entry(top, width=20, font=("Arial", 15), borderwidth=1, relief="solid", justify="center")
    entry.grid(column=0, row=1, columnspan=2, padx=3, pady=5)

    mibol = Label(top, text="Miből", font=("Arial", 20), bg="#a3cef1")
    mibol.grid(column=0, row=2, pady=5)

    mibe = Label(top, text="Mibe", font=("Arial", 20), bg="#a3cef1")
    mibe.grid(column=1, row=2, columnspan=2, pady=5)

    options = ["Milliméter", "Centiméter", "Deciméter", "Méter", "Kilométer"]
    clicked_from = StringVar()
    clicked_from.set("Méter")
    drop = OptionMenu(top , clicked_from , *options)
    drop.grid(column=0, row=3, padx=5, pady=10)

    clicked_to = StringVar()
    clicked_to.set("Kilométer")
    drop_to = OptionMenu(top, clicked_to, *options)
    drop_to.grid(column=1, row=3, padx=5, pady=10)

    szamol_button = Button(top, text="Számol", bg="#0d3b66", font=("Arial", 12), fg="white", command=show)
    szamol_button.grid(column=0, row=4, padx=3, pady=5)

    back_button = Button(top, text="Bezár", bg="#0d3b66", font=("Arial", 12), fg="white", command=top.destroy)
    back_button.grid(column=1, row=4, padx=3, pady=5)

    eredm = Label(top, text="", font=("Arial", 20), bg="#a3cef1")
    eredm.grid(column=0, row=5, columnspan=2, pady=10)


#tömeg ablak létrehozása
def tomeg():
    #mértékegységek érték adása
    def show(): 
        ertek = float(entry.get())  
        mibol = clicked_from.get()  
        mibe = clicked_to.get()  
        atvaltas_ertek = {
            "Milligramm": 1,
            "Gramm": 10,
            "Dekagramm": 100,
            "Kilogramm": 10000,
            "Tonna": 10000000
        }
        result = convert(ertek, mibol, mibe, atvaltas_ertek)
        eredm.config(text=f"Eredmény: {result} {mibe}")
    
    #tömeg ablak elemeinek létrehozása, elrendezése, dizájnolása
    top = Toplevel()
    top.title("Tömeg átváltás")
    top.config(bg="#a3cef1")

    entry = Entry(top, width=20, font=("Arial", 15), borderwidth=1, relief="solid", justify="center")
    entry.grid(column=0, row=1, columnspan=2, padx=3, pady=5)

    mibol = Label(top, text="Miből", font=("Arial", 20), bg="#a3cef1")
    mibol.grid(column=0, row=2, pady=5)

    mibe = Label(top, text="Mibe", font=("Arial", 20), bg="#a3cef1")
    mibe.grid(column=1, row=2, columnspan=2, pady=5)


    options = ["Milligramm", "Gramm", "Dekagramm", "Kilogramm", "Tonna"]
    clicked_from = StringVar()
    clicked_from.set("Kilogramm")
    drop = OptionMenu(top , clicked_from , *options)
    drop.grid(column=0, row=3, padx=5, pady=10)

    clicked_to = StringVar()
    clicked_to.set("Dekagramm")
    drop_to = OptionMenu(top, clicked_to, *options)
    drop_to.grid(column=1, row=3, padx=5, pady=10)

    szamol_button = Button(top, text="Számol", bg="#0d3b66", font=("Arial", 12), fg="white", command=show)
    szamol_button.grid(column=0, row=4, padx=3, pady=5)

    back_button = Button(top, text="Bezár", bg="#0d3b66", font=("Arial", 12), fg="white", command=top.destroy)
    back_button.grid(column=1, row=4, padx=3, pady=5)

    eredm = Label(top, text="", font=("Arial", 20), bg="#a3cef1")
    eredm.grid(column=0, row=5, columnspan=2, pady=10)


#Űrmérték ablak létrehozása
def urmerek():
    #mértékegységek érték adása
    def show(): 
        ertek = float(entry.get())  
        mibol = clicked_from.get()  
        mibe = clicked_to.get()  
        atvaltas_ertek = {
            "Mililiter": 1,
            "Centiliter": 10,
            "Deciliter": 100,
            "Liter": 1000,
            "Hektoliter": 100000
        }
        result = convert(ertek, mibol, mibe, atvaltas_ertek)
        eredm.config(text=f"Eredmény: {result} {mibe}")
    
    #űrmérték ablak elemeinek létrehozása, elrendezése, dizájnolása
    top = Toplevel()
    top.title("Űrmérték átváltás")
    top.config(bg="#a3cef1")

    entry = Entry(top, width=20, font=("Arial", 15), borderwidth=1, relief="solid", justify="center")
    entry.grid(column=0, row=1, columnspan=2, padx=3, pady=5)

    mibol = Label(top, text="Miből", font=("Arial", 20), bg="#a3cef1")
    mibol.grid(column=0, row=2, pady=5)

    mibe = Label(top, text="Mibe", font=("Arial", 20), bg="#a3cef1")
    mibe.grid(column=1, row=2, columnspan=2, pady=5)


    options = ["Mililiter", "Centiliter", "Deciliter", "Liter", "Hektoliter"]
    clicked_from = StringVar()
    clicked_from.set("Liter")
    drop = OptionMenu(top , clicked_from , *options)
    drop.grid(column=0, row=3, padx=5, pady=10)

    clicked_to = StringVar()
    clicked_to.set("Deciliter")
    drop_to = OptionMenu(top, clicked_to, *options)
    drop_to.grid(column=1, row=3, padx=5, pady=10)

    szamol_button = Button(top, text="Számol", bg="#0d3b66", font=("Arial", 12), fg="white", command=show)
    szamol_button.grid(column=0, row=4, padx=3, pady=5)

    back_button = Button(top, text="Bezár", bg="#0d3b66", font=("Arial", 12), fg="white", command=top.destroy)
    back_button.grid(column=1, row=4, padx=3, pady=5)

    eredm = Label(top, text="", font=("Arial", 20), bg="#a3cef1")
    eredm.grid(column=0, row=5, columnspan=2, pady=10)



#fő ablak dizájnolása, elemek létrehozása
label_szoveg = Label(root, text="Válaszd ki mit szeretnél átváltatni!", font=("Arial", 20), bg="#a3cef1")
label_szoveg.grid(column=0, row=1, columnspan=2, pady=10)

hossz_button = Button(root, text="Hosszúság átváltás", bg="#0d3b66", font=("Arial", 12), fg="white", command=hossz)
hossz_button.grid(column=0, row=2, padx=5, pady=10)

tomeg_button = Button(root, text="Tömeg átváltás", bg="#0d3b66", font=("Arial", 12), fg="white", command=tomeg)
tomeg_button.grid(column=1, row=2, padx=5, pady=10)

urmertek_button = Button(root, text="Űrmérték átváltás", bg="#0d3b66", font=("Arial", 12), fg="white", command=urmerek)
urmertek_button.grid(column=2, row=2, padx=5, pady=10)

stop_button = Button(root, text="Kilépés", bg="#0d3b66", font=("Arial", 12), fg="white", command=root.destroy)
stop_button.grid(column=1, row=3, padx=5, pady=10)

# Futtatás
root.mainloop()