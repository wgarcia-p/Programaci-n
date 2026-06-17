from tkinter import *
from   tkinter import ttk

def mostrar():
    etiqueta.config(
        text=(combo.get())
    )

ventana = Tk()
ventana.title("ComboBox y Label")
ventana.geometry("400x200")

combo = ttk.Combobox(ventana,
     state="readonly"
)
combo["values"] =(
    "Toyota",
    "Honda",
    "Mazda"
)
combo.current(0)
combo.pack(pady=10)

boton = Button(
    ventana,
    text=("Mostrar"),
    command=mostrar
)
boton.pack()

etiqueta = Label(
    ventana,
    text="Marcas"
)
etiqueta.pack(pady=10)

ventana.mainloop()  
