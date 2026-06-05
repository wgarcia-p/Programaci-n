from tkinter import *

def mostrar():
    print(caja.get())

ventana = Tk()
ventana.title("get") 
ventana.geometry("300x300")

caja = Entry(ventana)
caja.pack()

BOTON1 = Button(
    ventana,
    text="Mostrar",
    command= mostrar
)
BOTON1.pack()

ventana.mainloop()