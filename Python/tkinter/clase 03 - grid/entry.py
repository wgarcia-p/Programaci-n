from tkinter import *

ventana = Tk()
ventana.title("ENTRY") 
ventana.geometry("300x300")

caja = Entry(ventana)
caja.grid(row=0,column=0)

ventana.mainloop()