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
combo.grid(row=0,column=0,padx=10,pady=10)

boton = Button(
    ventana,
    text=("Mostrar"),
    command=mostrar
)
boton.grid(row=0,column=1,padx=10,pady=10)

etiqueta = Label(
    ventana,
    text="Marcas"
)
etiqueta.grid(row=1, column=0, padx=10,pady=10)

ventana.mainloop()  
