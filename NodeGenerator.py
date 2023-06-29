import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def buscarRegistro(nombre, n_max):
    filename = 'vgsales.csv'
    data = pd.read_csv(filename, header=0)

    registro = data[data['Name'].str.upper() == nombre.upper()]
    if not registro.empty:
        # Extraer género y plataforma del registro
        genero = registro['Genre'].values[0]
        plataforma = registro['Platform'].values[0]
        GYP = [genero, plataforma]

        filtro = ((data['Genre'] == GYP[0])) & ((data['Platform'] == GYP[1]))
        fil = data[filtro]
        num_registros = fil.shape[0]
        print(num_registros)        
        print(fil)
    else:
        print("No se encontró ningún registro con ese nombre.")
        fil = pd.DataFrame()

    G = nx.Graph()

    #limitar el numero de notos a 100
    if num_registros > n_max:
        num_registros = n_max
        fil = fil.head(n_max)
    
    for index, row in fil.iterrows():
        G.add_node(row['Name'], genre=row['Genre'], platform=row['Platform'])

    for index, row in fil.iterrows():
        for index2, row2 in fil.iterrows():
            if row['Name'] != row2['Name']:
                G.add_edge(row['Name'], row2['Name'], weight=1)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=100, node_color='blue')
    nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='black')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    plt.axis('off')
    plt.show()