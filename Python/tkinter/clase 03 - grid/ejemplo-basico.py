from tkinter import *

ventana = Tk()
ventana.title("Ejemplo básico")
ventana.geometry("300x200")

Label(ventana, text="Nombre").grid(row=0, column=0)
Label(ventana, text="Willy").grid(row=0,column=1)
Label(ventana, text="GARCÍA").grid(row=0,column=2)

ventana.mainloop()
