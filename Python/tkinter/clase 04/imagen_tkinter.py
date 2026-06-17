from tkinter import *

ventana = Tk()
ventana.title("Ejemplo básico")
ventana.geometry("300x200")

#direccion = "C:/Users/Willy/Documents/Repositorios/Programaci-n/Python/tkinter/clase 04/logo.png"
direccion= "C:\Users\Willy\Documents\Repositorios\Programaci-n\Python\tkinter\clase 04\logo.png"
direccion= direccion.replace("/","\\") 

imagen = PhotoImage(file= direccion)
imagen_pequena = imagen.subsample(7,7) #2/2 mitad, 3/3 tercera parte, 4/4 cuarta parte

label_imagen = Label(ventana, image=imagen_pequena)
label_imagen.grid(row=0,column=0)

ventana.mainloop()