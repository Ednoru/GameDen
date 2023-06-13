import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def getNode(n):
    filename = './HITO2/vgsales.csv'
    data = pd.read_csv(filename, header=0)

    nodes = data.sample(int(n), random_state=1)

    #Imprime 'n' nodos aleatorios
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