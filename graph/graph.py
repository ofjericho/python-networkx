import networkx
from matplotlib.pyplot import draw, show


graph = networkx.Graph()


def create_nodes(*nodes):
    for node in nodes:
        graph.add_node(node)


def create_edges(edges):
    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=0.5)


def plot_graph():
    networkx.draw(graph, with_labels=True)
    draw()
    show()
