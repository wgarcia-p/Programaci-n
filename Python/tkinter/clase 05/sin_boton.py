from tkinter import *
from tkinter import ttk

ventana =Tk()
ventana.title("Evento ComboBox")
ventana.geometry("400x200")

def cambiar (event):
    etiqueta.config(
        text = combo.get()
    )


combo = ttk.Combobox(
    ventana,
    state= "readonly"
)

combo["values"] = (
    "Enero",
    "Febrero",
    "Marzo"
)
combo.current(0)
combo.grid(row=0,column=0,padx=10,pady=10)

combo.bind(
    "<<ComboboxSelected>>",
    cambiar
)

etiqueta = Label(
    ventana,
    text="Seleccione un mes de la lista"
)
etiqueta.grid(row=1,column=0,padx=10,pady=10)


ventana.mainloop()