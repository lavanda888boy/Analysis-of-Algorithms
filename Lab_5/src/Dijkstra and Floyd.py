import sys
from random import randint
from time import time


# Dijkstra algorithm for the shortest path from the source
def Dijkstra_algorithm(vertices, edges):
    
    def to_be_visited():
        v = -10
        for index in range(num_of_vertices):
            if (visited_and_distance[index][0] == 0) and (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
                v = index
        return v

    num_of_vertices = len(vertices[0])

    visited_and_distance = [[0, 0]]
    for i in range(num_of_vertices - 1):
        visited_and_distance.append([0, sys.maxsize])

    for vertex in range(num_of_vertices):
        to_visit = to_be_visited()

        for neighbor_index in range(num_of_vertices):
            if (vertices[to_visit][neighbor_index] == 1) and (visited_and_distance[neighbor_index][0] == 0):
                new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]

                if visited_and_distance[neighbor_index][1] > new_distance:
                    visited_and_distance[neighbor_index][1] = new_distance
        
            visited_and_distance[to_visit][0] = 1
    
    return visited_and_distance


# Floyd-Warshall algorithm for the shortest path between all the vertices
def Floyd_Warshall_algorithm(vertices, edges):
    num_of_vertices = len(vertices[0])
    distance = edges

    for x in range(num_of_vertices - 1):
        for y in range(num_of_vertices - 1):
            if (vertices[x][y] == 0) and (x != y):
                distance[x][y] = sys.maxsize

    for k in range(num_of_vertices):
        for i in range(num_of_vertices):
            for j in range(num_of_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print(distance)


dense_coefficient = 80
sparse_coefficient = 30

'''
def generateGraph(size, coef):
    v = list()
    e = [[0 for _ in range(size)]] * size

    for i in range(size):

        for j in range(size):
            if i != j:
                choice = randint(0, 100)
                v[i][j] = choice
        print(v)

    print(v)

generateGraph(5)
'''

def current_time_millis():
    return time() * 1000


# testing the algorithms
input_sizes = [100, 1000, 5000, 1000, 10000, 50000]
dijkstra_dense, dijkstra_sparse = list(), list()
floyd_dense, floyd_sparse = list(), list()

start_time, end_time = 0, 0

# testing on dense graphs
for index in range(len(input_sizes)):
    vertices, edges = generateGraph(input_sizes[index], dense_coefficient)

    start_time = current_time_millis()
    Dijkstra_algorithm(vertices, edges)
    end_time = current_time_millis()

    dijkstra_dense.append(round(end_time - start_time), 3)

    start_time = current_time_millis()
    Floyd_Warshall_algorithm(vertices, edges)
    end_time = current_time_millis()
    
    floyd_dense.append(round(end_time - start_time), 3)


# testing on sparse graphs
for index in range(len(input_sizes)):
    vertices, edges = generateGraph(input_sizes[index], sparse_coefficient)

    start_time = current_time_millis()
    Dijkstra_algorithm(vertices, edges)
    end_time = current_time_millis()

    dijkstra_sparse.append(round(end_time - start_time), 3)

    start_time = current_time_millis()
    Floyd_Warshall_algorithm(vertices, edges)
    end_time = current_time_millis()
    
    floyd_sparse.append(round(end_time - start_time), 3)