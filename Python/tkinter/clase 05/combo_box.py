from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("ComboBox Basico")
ventana.geometry("400x200")

combo = ttk.Combobox(ventana)

combo["values"]=(
    "01. Guatemala",
    "02. El Salvador",
    "03. Honduras",
    "04. Nicaragua"
)
combo.current(3)
combo.pack(pady=20)
ventana.mainloop()