from tkinter import *
from   tkinter import ttk

def mostrar():
    print(combo.get())

ventana = Tk()
ventana.title("Leer combobox")
ventana.geometry("400x200")

combo = ttk.Combobox(ventana)
combo["values"] =(
    "Rojo",
    "Azul",
    "Verde"
)
combo.pack(pady=10)

boton = Button(
    ventana,
    text=("Mostrar en consola"),
    command=mostrar
)
boton.pack()    
ventana.mainloop()  