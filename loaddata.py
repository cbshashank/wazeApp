from collections import defaultdict

#Loads all of the nodes into a dictionary where the key represents the node ID and value represents the coordinates
# as a 2 element tuple
def loadNodes(nodeFile):
    nodeDict = {}
    file=open(nodeFile, "r")
    for node in file:
        individualNode=node.split()
        nodeID=int(individualNode[0])
        coordinates=(individualNode[1],individualNode[2])
        nodeDict[nodeID]=coordinates
    return nodeDict

#Selection 1: maps edgeIds to nodeIDs
#Selectoin 2: maps edgeIds to distance
def loadEdges(edgeFile,selection):
    edgeConnections = {}
    edgeDistance={}
    file = open(edgeFile, "r")
    for edge in file:
        individualEdge = edge.split()
        edgeID = int(individualEdge[0])
        connections = (int(individualEdge[1]), int(individualEdge[2]))
        distance=float(individualEdge[3])
        edgeConnections[edgeID] = connections
        edgeDistance[edgeID]=distance
    if selection==1:
        return edgeConnections
    if selection==2:
        return edgeDistance


#This returns a dict that maps each node ID to its edgeIDs
def mapAdjacent(edges):
    nodeEdges = defaultdict(list)
    for edge in edges:
         nodeEdges[(edges[edge][0])].append(edge)
         nodeEdges[(edges[edge][1])].append(edge)
    return nodeEdges



def loadPoints(nodefile, edgefile):
    coordinateDict = loadNodes(nodefile)
    edgeConnections = loadEdges(edgefile, 1)
    nodeAdj = mapAdjacent(edgeConnections)



