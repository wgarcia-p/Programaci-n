import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primer label") #nombre
ventana.geometry("600x200") #dimensiones de la ventana
texto = tk.Label( #declaramos el label
    ventana,    
    text="HOLA MUNDO", #texto del label
    fg="black", #color de la letra
    bg="turquoise1", #color de fondo 
    font=("Arial",25) #atributos del texto
)
texto1 = tk.Label(
    ventana,    
    text="ESTOY ESTUDIANDO",
    fg="green",
    bg="yellow",
    font=("Times New Roman",25, "bold")
)
texto2 = tk.Label(
    ventana,    
    text="PROGRAMACION EN PYTHON",
    fg="purple",
    font=("Courier New",25,"italic")
)
texto.pack() #se muestra el label
texto1.pack()
texto2.pack()
ventana.mainloop()