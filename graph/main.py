from graph import graph

if __name__ == "__main__":

    graph.create_nodes(1, 2, 3, 4)

    graph.create_edges({(1, 2), (1, 3), (3, 4)})

    graph.plot_graph()
