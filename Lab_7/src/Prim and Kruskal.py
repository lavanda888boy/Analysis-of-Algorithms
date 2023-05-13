import sys
from random import randint
from time import time
 
# class representing the graph iteslf which contins methods form Prim's 
# and Kruskal's algorithms implementation
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    # block of methods for implementing Prim's algorithm
    def minKey(self, key, mstSet):
        min = sys.maxsize
 
        for v in range(self.V):
            if (key[v] < min) and (mstSet[v] == False):
                min = key[v]
                min_index = v
 
        return min_index
 
    def PrimMST(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V 
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1 
 
        for index in range(self.V):
            u = self.minKey(key, mstSet)

            mstSet[u] = True
 
            for v in range(self.V):
                if (self.graph[u][v] > 0) and (mstSet[v] == False) and (key[v] > self.graph[u][v]):
                    key[v] = self.graph[u][v]
                    parent[v] = u
 
        self.printMST(parent)

    
    # block of methods used for implementing Kruskal algorithm
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        
        return parent[i]
 

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
 

    def KruskalMST(self):
        result = []
        i = 0
        result_index = 0
 
        self.graph = sorted(self.graph, key=lambda item: item[2])
 
        parent = []
        rank = []
 
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        while result_index < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            if x != y:
                result_index = result_index + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)


def generateGraph(size, coef):
    v = list()
    e = list()
    
    for x in range(size):
        v.append(list())
        for y in range(size):
            if x == y:
                v[x].append(0)
            else:
                choice = randint(0, 100)
                
                if choice <= coef:
                    v[x].append(1)
                else:
                    v[x].append(0)
    
    for x in range(size):
        e.append(list())
        for y in range(size):
            if v[x][y] != 0:
                e[x].append(randint(10, 100))
            else:
                e[x].append(0)

    return e


def current_time_millis():
    return time() * 1000


if __name__ == '__main__':

    
    g = Graph(4)
 
    #g.primMST()

    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.KruskalMST()