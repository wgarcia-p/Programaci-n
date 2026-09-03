import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x200")

# Botón alineado a la izquierda
btn_izq = tk.Button(ventana, text="Izquierda")
btn_izq.grid(row=0, column=0, sticky="w")


ventana.rowconfigure(1, minsize=20)

# Entry centrado (sin sticky queda centrado)
entry_centro = tk.Entry(ventana)
entry_centro.grid(row=2, column=0)

ventana.rowconfigure(3, minsize=20)

# Botón alineado a la derecha
btn_der = tk.Button(ventana, text="Derecha")
btn_der.grid(row=4, column=0, sticky="e")

ventana.mainloop()
