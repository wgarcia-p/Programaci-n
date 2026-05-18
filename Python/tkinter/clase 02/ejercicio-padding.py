import tkinter as tk

ventana = tk.Tk()

ventana.title("Ejercicio padding") #nombre
ventana.geometry("800x800") #dimensiones de la ventana

texto1= tk.Label(
    ventana,
    text="VENTAS",
 
    bg="DeepSkyBlue2",
    fg="gray26",
    font=("Times New Roman",25),
    anchor="n", #orientacion del texto dentro del label
    padx= 30, #espacio del borde hacia el texto en horizontal
    pady= 30,  #espacio del borde hacia el texto en vertical
    bd=3, #grosor del borde
    relief="raised" #tipo de borde
)

texto2 = tk.Label(
    ventana,
    text="INVENTARIO",
 
    bg="#36ADA3",
    fg="gray26",
    font=("Times New Roman",25),
    anchor="n", #orientacion del texto dentro del label
    padx= 30, #espacio del borde hacia el texto en horizontal
    pady= 30,  #espacio del borde hacia el texto en vertical
    bd=3,
    relief="groove"
)


texto3 = tk.Label(
    ventana,
    text="CLIENTES",
 
    bg="#C3A18E",
    fg="#202940",
    font=("Times New Roman",25),
    anchor="n", #orientacion del texto dentro del label
    padx= 30, #espacio del borde hacia el texto en horizontal
    pady= 30,  #espacio del borde hacia el texto en vertical
    bd=3,
    relief="sunken"
)


texto4 = tk.Label(
    ventana,
    text="REPORTES",
 
    bg="#FAE7CB",
    fg="black",
    font=("Times New Roman",25),
    anchor="n", #orientacion del texto dentro del label
    padx= 30, #espacio del borde hacia el texto en horizontal
    pady= 30,  #espacio del borde hacia el texto en vertical
    bd=3,
    relief="solid"
)



texto1.pack(pady=10)
texto2.pack(pady=10)
texto3.pack(pady=10)
texto4.pack(pady=10)
ventana.mainloop()