import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def getNode(juego, n):
    filename = 'vgsales.csv'
    data = pd.read_csv(filename, header=0)

    # Filtrar los juegos que coincidan con el nombre ingresado
    juegos_encontrados = data[data['Name'].str.contains(juego, case=False)]

    # Seleccionar la cantidad de nodos especificada
    nodes = juegos_encontrados.sample(n, random_state=1)

    # Crear el grafo vacío
    G = nx.Graph()

    # Agregar los nodos del dataset
    for index, row in nodes.iterrows():
        G.add_node(row['Name'], genre=row['Genre'])

    # Agregar las aristas del dataset
    for index, row in nodes.iterrows():
        G.add_edge(row['Name'], row['Genre'])

    # Dibujar el grafo
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw_networkx(G, pos, node_size=1000, alpha=0.8, node_color='lightblue', with_labels=True, arrows=True)
    labels = nx.get_node_attributes(G, 'genre')
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_family='sans-serif')
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=1.0, edge_color='black')

    # Mostrar el grafo
    plt.title('Relación de juegos con sus géneros principales')
    plt.show()