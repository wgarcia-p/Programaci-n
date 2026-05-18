import tkinter as tk

ventana = tk.Tk()

ventana.title("LABEL 2") #nombre
ventana.geometry("800x800") #dimensiones de la ventana

texto = tk.Label(
    ventana,
    text="Inventario\nEmpresa UNO\nVersión 1",
 
    bg="DeepSkyBlue2",
    fg="gray26",
    font=("Times New Roman",25),
    anchor="n", #orientacion del texto dentro del label
    padx= 100, #espacio del borde hacia el texto en horizontal
    pady= 100  #espacio del borde hacia el texto en vertical
)
texto.pack()
ventana.mainloop()