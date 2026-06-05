from tkinter import *

def mostrar():
    nota = int(caja.get())
    if nota >= 60:
        etiqueta.config(
        text= "APROBADO"
        )
    else:
        etiqueta.config(
        text= "REPROBADO"
        )
        
ventana = Tk()
ventana.title("ENTRY") 
ventana.geometry("300x300")

caja = Entry(
    ventana,
    font=("Times New Roman", 18)
    )
caja.pack()

etiqueta = Label(
    ventana,
    font=("Times New Roman", 18),
    text="RESULTADO"
)
etiqueta.pack()

boton = Button(
    ventana,
    font=("Times New Roman", 18),
    text="MOSTRAR",
    command= mostrar
)
boton.pack()
ventana.mainloop()