import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Conversión a Entero")
ventana.geometry("350x200")

# Variable para mostrar resultado
resultado = tk.StringVar()

# Etiqueta de instrucción
label = tk.Label(ventana, text="Ingrese un número:")
label.pack(pady=5)

# Campo de entrada (una sola línea)
entry = tk.Entry(ventana)
entry.pack(pady=5)

# Etiqueta donde se mostrará el resultado
label_resultado = tk.Label(ventana, textvariable=resultado, font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

# Función del botón
def convertir():
    contenido = entry.get().strip()
    
    try:
        numero = int(contenido)
        resultado.set(f"Número entero: {numero}")
    except ValueError:
        resultado.set("Error: Ingrese un número válido")

# Botón
boton = tk.Button(ventana, text="Convertir", command=convertir)
boton.pack(pady=10)

ventana.mainloop()