from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font
import tkinter.font as font
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


#input(nro de nodos)
def obtener_valor():
    valor = entry.get()
    print("El valor ingresado es:", valor)


#ventana
ventana=tk.Tk()
ventana.title("GamerDen")
ventana.geometry("500x350")
ventana.resizable(True,True)

#fondo
imagen=Image.open("./img/fondo.jpeg")
imagen = imagen.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
imagen_de_fondo = ImageTk.PhotoImage(imagen)
fondo = tk.Label(ventana, image=imagen_de_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

#Nombre de la app
ruta_fuente = 'angrybirds-regular.ttf'  # Reemplaza con la ruta correcta del archivo de fuente
fuente_personalizada = font.Font(family='AngryBirds', size=20)
texto = "GamerDen"
label_texto = tk.Label(ventana, text=texto, fg="black", font=fuente_personalizada)
label_texto.grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)
fuentes_disponibles = font.families()
print(fuentes_disponibles)

#Colocar el input en la interfaz
label = tk.Label(ventana, text="Ingrese el nro de nodos:")
label.grid(row=1, column=0)

entry = tk.Entry(ventana)
entry.grid(row=1, column=1)

boton = tk.Button(ventana, text="Obtener Valor", command=obtener_valor)
boton.grid(row=1, column=2)


#Carga la ventana
ventana.mainloop()

########################################################################################################

#Codigo
filename = 'vgsales.csv'
data = pd.read_csv(filename, header=0)

nodes = data.sample(10)

#Imprime 500 nodos aleatorios
print (nodes)                                                                                                                                                                                                                                                                                                                                                                                                   #Creamos el grafo vacio
G = nx.Graph()

#Agregamos los nodos del dataset
for index, row in nodes.iterrows():
    G.add_node(row['Name'], data=row['Genre'])

#Agregamos las aristas del dataset
for index, row in nodes.iterrows():
    G.add_edge(row['Name'], row['Genre'])

#Dubujamos el grafo
pos = nx.spring_layout(G, k=0.5, iterations=50)
nx.draw_networkx(G, pos, node_size=1000, alpha=0.8, node_color='lightblue', with_labels=True, arrows=True)
labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_family='sans-serif')
nx.draw_networkx_edges(G, pos, width=1.0, alpha=1.0, edge_color='black')

#Mostramos el grafo
plt.title('Relación de juegos con sus géneros principales')
plt.show()