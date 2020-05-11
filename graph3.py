'''
Vertices: A, B, C, D, E
Edges: AB, AD, BC, BD, CD, DE
'''

#graph = dict('A': ['B','D'],
#             'B': ['A','C','D'],#
#             'C': ['B','D'],
#             'D': ['A','B','C','E'],
#             'E': ['D'])

class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    def __init__(self):
        pass

    def add_edge():
