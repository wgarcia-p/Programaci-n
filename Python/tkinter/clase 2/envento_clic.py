import tkinter as tk

ventana = tk.Tk()
ventana.title("EVENTO")
ventana.geometry("400x200")

mensaje = tk.Label(
    ventana, text="Texto original",
    font=("arial",18)
)
mensaje.pack()

def saludar():
    mensaje.config(
    text="HOLA BIENVENIDO A POE"
    )

boton = tk.Button(
    ventana,
    text="Presioname",
    padx=10,
    pady=10,
    bg="#767F9E",
    font=("Arial",16),
    command=saludar
)

boton.pack(pady=25)
ventana.mainloop()