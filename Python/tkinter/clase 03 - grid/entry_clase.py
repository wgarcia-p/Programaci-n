from tkinter import *
ventana = Tk()

ventana.title("Ejercicio")
ventana.geometry("500x500")

def mostra():

    usuario = caja1.get()
    contraseña = caja2.get()
    print(usuario)
    print(contraseña)

Label(ventana,
      text="Usuario",
      font=("Times New Roman", 20)
      ).grid(row=0,column=0,padx=5,pady=10)
caja1 = Entry(ventana,
      font=("Times New Roman", 15)
      )

caja1.grid(row=0,column=1)

Label(ventana,
      text="Contraseña",
      font=("Times New Roman", 20)
      ).grid(row=1,column=0,padx=5,pady=10)
caja2 = Entry(ventana,
      font=("Times New Roman", 15),
      show=("*")
      )

caja2.grid(row=1,column=1)

Button(
    ventana,
    text="[INGRESAR]",
    font=("Times New Roman", 24),
    padx=10,
    pady=10,
    bg="#D7EBDD",
    command=mostra,
).grid(row=2,column=0,padx=5,pady=10)

ventana.mainloop() 