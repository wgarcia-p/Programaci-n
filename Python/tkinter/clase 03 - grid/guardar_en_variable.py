from tkinter import *

def mostrar():
    print(caja.get())

ventana = Tk()
ventana.title("get") 
ventana.geometry("300x300")


mensaje = Label(
    ventana,
    text="Ingrese su contraseña",
    font=("Times New Roman", 14),
    fg="black",
    bg="#ECE0D1",
    padx=30,
    pady=30,
    bd=3,
    relief="solid"
)
mensaje.pack()

caja = Entry(
    ventana, 
    width=35, 
    show="*",
    font=("Times New Roman", 14),
    fg="black",
    bg="#ECE0D1"
    ) #width cambia el ancho de la caja
caja.pack(pady=30)


BOTON1 = Button(
    ventana,
    text="Mostrar",
    command= mostrar
)
BOTON1.pack()

ventana.mainloop()