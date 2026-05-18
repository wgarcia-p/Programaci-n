import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primer label") #nombre
ventana.geometry("300x200") #dimensiones de la ventana
texto = tk.Label(
    ventana,    
    text="HOLA MUNDO"
    
)
texto.pack()
ventana.mainloop()