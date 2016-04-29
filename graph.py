# Modified code from https://github.com/Pent00/YenKSP.

import os
import json
import random

class DiGraph:
    ## The location that the graph data is stored as json objects.
    _directory_data = "/Users/shashank/Documents/school/Spring2016/ds2/wazeApp2/data/json/"

    INFINITY = 10000

    UNDEFINDED = None

    _name = "graph"
    _data = {}

    def __init__(self, name=None):
        if name:
            self._name = name
        self.load()
        return

    def __getitem__(self, node):
        if self._data.has_key(node):
            return self._data[node]
        else:
            return None

    def __iter__(self):
        return self._data.__iter__()

    ## Adds a node to the graph
    def add_node(self, node):
        if self._data.has_key(node):
            return False

        self._data[node] = {}
        return True

    ## Adds a edge to the graph

    def add_edge(self, node_from, node_to, cost=None):
        if not cost:
            cost = random.randrange(1, 11)

        self.add_node(node_from)
        self.add_node(node_to)

        self._data[node_from][node_to] = cost
        return

    ## Removes an edge from the graph.
    def remove_edge(self, node_from, node_to, cost=None):
        if not self._data.has_key(node_from):
            return -1

        if self._data[node_from].has_key(node_to):
            if not cost:
                cost = self._data[node_from][node_to]

                if cost == self.INFINITY:
                    return -1
                else:
                    self._data[node_from][node_to] = self.INFINITY
                    return cost
            elif self._data[node_from][node_to] == cost:
                self._data[node_from][node_to] = self.INFINITY

                return cost
            else:
                return -1
        else:
            return -1

    ## Populates the graph with the data of the graph indentifier.
    def load(self):
        path_json = "%s%s.json" % (self._directory_data, self._name)
        if not os.path.exists(path_json):
            return False

        fhandle = open(path_json, 'r')
        self._data = json.loads(fhandle.read())
        fhandle.close()

        return True
