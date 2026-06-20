import matplotlib.pyplot as plt
import networkx as nx

plt.figure(figsize=(5,2))
G = nx.DiGraph()
posiciones ={}
G.add_edge("S", "A1", capacity=2)
G.add_edge("A1", "B2", capacity=1)
G.add_edge("B2","T",capacity=3)

posiciones["S"] = (0,0)
posiciones["A1"] = (1,0)
posiciones["B2"] = (2,0)
posiciones["T"] = (3,0)

etiquetas = {
    (u, v): d["capacity"]
    for u, v, d in G.edges(data=True)
    if d["capacity"] != 1
}


nx.draw(
    G,
    pos=posiciones,
    with_labels=True,
    node_color="skyblue",
    node_size=2500,
    font_size=14,
    font_weight="bold",
    width=2,
    arrowsize=25
)

nx.draw_networkx_edge_labels(
    G,
    posiciones,
    edge_labels=etiquetas,
    font_size=12
)

plt.title("Camino de aumento")
plt.title(
    "Camino de aumento con: k = 2, b = 3",
    fontsize=14,
    fontweight="bold"
)
plt.axis("off")
plt.savefig("camino_aumento.png", dpi=300, bbox_inches="tight")