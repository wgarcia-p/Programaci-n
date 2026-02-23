import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("400x300")

# Título
titulo = tk.Label(ventana, text="Formulario Simple", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Label
label = tk.Label(ventana, text="Ingrese su texto:")
label.pack(pady=5)

# Textbox
textbox = tk.Text(ventana, height=8, width=40)
textbox.pack(pady=10)

# Botón
def on_click():
    contenido = textbox.get("1.0", tk.END)
    print("Texto ingresado:", contenido)

boton = tk.Button(ventana, text="Enviar", command=on_click)
boton.pack(pady=10)

# Iniciar loop
ventana.mainloop()