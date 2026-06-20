import matplotlib.pyplot as plt
import networkx as nx


def visualizar_backups(grafo, antenas):
    posiciones = {}
    posiciones["S"] = (0, len(antenas)/2)
    posiciones["T"] = (3, len(antenas)/2)
    
    for i, antena in enumerate(antenas,start=1):
        posiciones[antena.getId()] = (1,i)
    
    for i, antena in enumerate(antenas,start=1):
        posiciones[antena.getDirigido()] = (2,i)

    colores = []

    for nodo in grafo.nodes():
        if nodo == "S":
            colores.append("lightgreen")
        elif nodo == "T":
            colores.append("salmon")
        elif nodo.startswith("A"):
            colores.append("skyblue")
        else:
            colores.append("orange")

    etiquetas = {
        (u,v): d["capacity"]
        for u,v,d in grafo.edges(data=True)
        if d["capacity"] != 1
    }

    nx.draw(
        grafo,
        pos=posiciones,
        with_labels=True,
        node_color=colores,
        node_size=1500,
        font_weight="bold",
        arrows=True
    )

    nx.draw_networkx_edge_labels(
        grafo,
        posiciones,
        edge_labels=etiquetas
    )

    plt.title("Red de Flujo")
    plt.axis("off")
    plt.savefig("grafo.png", bbox_inches="tight")