import tkinter as tk

ventana = tk.Tk()
ventana.title("Botón")
ventana.geometry("300x200")

boton = tk.Button(
    ventana,
    text="Presioname",
    padx=10,
    pady=10,
    bg="#767F9E",
    font=("Arial",16)
)
boton.pack(pady=25)
ventana.mainloop()