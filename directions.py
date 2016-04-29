from graph import DiGraph
import algorithms

def getDirections(start, end):

    # Load the graph
    G = DiGraph("shortestPath")



    # Get 3 shortest paths from the graph.
    items = algorithms.ksp_yen(G, start, end, 3)
    return items

