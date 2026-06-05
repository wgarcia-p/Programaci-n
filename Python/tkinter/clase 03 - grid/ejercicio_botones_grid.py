from tkinter import *
import tkinter as tk

ventana = tk.Tk()
ventana.title("servidor") 
ventana.geometry("1000x1000")


mensaje = tk.Label(
    ventana,
    text="Elija un color",
    font=("Times New Roman", 20),
    fg="black",
    bg="#F1E2D1",
    padx=30,
    pady=30,
    bd=3,
    relief="solid"
)
def color1():
    mensaje.config(
        text="Cafe",
        font=("Times New Roman", 20),
        fg="black",
        bg="#8A5F41",
        padx=30,
        pady=30,
        bd=3,
        relief="solid"

    )

boton = tk.Button(
    ventana,
    text="Cafe",
    padx=10,
    pady=10,
    bg="#8A5F41",
    font=("Times New Roman", 18),
    command=color1
)

def color2():
    mensaje.config(
        text="Naranja",
        font=("Times New Roman", 20),
        fg="black",
        bg="#EA7300",
        padx=30,
        pady=30,
        bd=3,
        relief="solid"

    )
boton2 = tk.Button(
    ventana,
    text="Naranja",
    padx=10,
    pady=10,
    bg="#EA7300",
    font=("Times New Roman", 18),
    command=color2
)

def color3():
    mensaje.config(
        text="Celeste",
        font=("Times New Roman", 20),
        fg="black",
        bg="#468A9A",
        padx=30,
        pady=30,
        bd=3,
        relief="solid"

    )
boton3 = tk.Button(
    ventana,
    text="Celeste",
    padx=10,
    pady=10,
    bg="#468A9A",
    font=("Times New Roman", 18),
    command=color3
)

def color4():
    mensaje.config(
        text="Negro",
        font=("Times New Roman", 20),
        fg="#EEEEEE",
        bg="black",
        padx=30,
        pady=30,
        bd=3,
        relief="solid"

    )
boton4 = tk.Button(
    ventana,
    text="Negro",
    padx=10,
    pady=10,
    fg="#EEEEEE",
    bg="black",
    font=("Times New Roman", 18),
    command=color4
)

def color5():
    mensaje.config(
        text="Verde",
        font=("Times New Roman", 20),
        fg="black",
        bg="#84994F",
        padx=30,
        pady=30,
        bd=3,
        relief="solid"

    )
boton5 = tk.Button(
    ventana,
    text="Verde",
    padx=10,
    pady=10,
    bg="#84994F",
    font=("Times New Roman", 18),
    command=color5
)

def color6():
    mensaje.config(
        text="Rojo",
        font=("Times New Roman", 20),
        fg="black",
        bg="#A72703",
        padx=30,
        pady=30,
        bd=3,
        relief="solid"

    )
boton6 = tk.Button(
    ventana,
    text="Rojo",
    padx=10,
    pady=10,
    bg="#A72703",
    font=("Times New Roman", 18),
    command=color6
)

def color7():
    mensaje.config(
        text="Morado",
        font=("Times New Roman", 20),
        fg="black",
        bg="#744577",
        padx=30,
        pady=30,
        bd=3,
        relief="solid"

    )
boton7 = tk.Button(
    ventana,
    text="Morado",
    padx=10,
    pady=10,
    bg="#744577",
    font=("Times New Roman", 18),
    command=color7
)

def color8():
    mensaje.config(
        text="Azul",
        font=("Times New Roman", 20),
        fg="black",
        bg="#2D3C59",
        padx=30,
        pady=30,
        bd=3,
        relief="solid"

    )
boton8 = tk.Button(
    ventana,
    text="Azul",
    padx=10,
    pady=10,
    bg="#2D3C59",
    font=("Times New Roman", 18),
    command=color8
)

def color9():
    mensaje.config(
        text="Amarillo",
        font=("Times New Roman", 20),
        fg="black",
        bg="#E4D329",
        padx=30,
        pady=30,
        bd=3,
        relief="solid"

    )
boton9 = tk.Button(
    ventana,
    text="Amarillo",
    padx=10,
    pady=10,
    bg="#E4D329",
    font=("Times New Roman", 18),
    command=color9
)



mensaje.grid(row=0,column=1)
boton.grid(row=1, column=0,pady=10)
boton2.grid(row=1, column=1)
boton3.grid(row=1, column=2)
boton4.grid(row=2, column=0,pady=10)
boton5.grid(row=2, column=1)
boton6.grid(row=2, column=2)
boton7.grid(row=3, column=0,pady=10)
boton8.grid(row=3, column=1)
boton9.grid(row=3, column=2)
ventana.mainloop() 