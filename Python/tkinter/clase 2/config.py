import tkinter as tk   
ventana = tk.Tk()
ventana.title("Uso de config")
ventana.geometry("300x200")

mensaje = tk.Label(
    ventana, text="Texto original"
)
mensaje.pack()

mensaje.config(
    text="Texto nuevo"
)
ventana.mainloop()