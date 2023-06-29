from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font
import tkinter.font as font
import NodeGenerator as ng

# ventana
ventana = tk.Tk()
ventana.title("GamerDen")
ventana.geometry("500x350")
ventana.resizable(True, True)

# fondo
imagen = Image.open("./GameDen/fondo.jpeg")
imagen = imagen.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
imagen_de_fondo = ImageTk.PhotoImage(imagen)
fondo = tk.Label(ventana, image=imagen_de_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Nombre de la app
ruta_fuente = 'angrybirds-regular.ttf'  # Reemplaza con la ruta correcta del archivo de fuente
fuente_personalizada = font.Font(family='AngryBirds', size=20)
texto = "GamerDen"
label_texto = tk.Label(ventana, text=texto, fg="black", font=fuente_personalizada)
label_texto.grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)
fuentes_disponibles = font.families()
print(fuentes_disponibles)

# Colocar el input en la interfaz
label_juego = tk.Label(ventana, text="Ingrese el nombre del juego:")
label_juego.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_juego = tk.Entry(ventana)
entry_juego.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

label_nodos = tk.Label(ventana, text="Ingrese la cantidad maxima de nodos:")
label_nodos.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

entry_nodos = tk.Entry(ventana)
entry_nodos.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

# boton para generar el grafo
boton = tk.Button(ventana, text="Generar grafo", command=lambda: ng.buscarRegistro(entry_juego.get(), int(entry_nodos.get())))
boton.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

# Carga la ventana
ventana.mainloop()