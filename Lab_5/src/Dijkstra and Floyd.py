import sys
from random import randint
from matplotlib.pyplot import plot
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


# coefficients for defining the number of edges in a graph
# thus declaring it as dense or sparse
dense_coefficient = 80
sparse_coefficient = 30


# function for creating a dense/sparse graph of a given size
def generateGraph(size, coef):
    v = random.randint(0, 1, size=(size, size))
    e = random.randint(1, 5, size=(size, size))
    
    for x in range(size):
        for y in range(size):
            if x == y:
                v[x][y] = 0
    print(v)
    return v, e


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

    dijkstra_dense.append(round(end_time - start_time, 3))

    start_time = current_time_millis()
    Floyd_Warshall_algorithm(vertices, edges)
    end_time = current_time_millis()
    
    floyd_dense.append(round(end_time - start_time, 3))


# testing on sparse graphs
for index in range(len(input_sizes)):
    vertices, edges = generateGraph(input_sizes[index], sparse_coefficient)

    start_time = current_time_millis()
    Dijkstra_algorithm(vertices, edges)
    end_time = current_time_millis()

    dijkstra_sparse.append(round(end_time - start_time, 3))

    start_time = current_time_millis()
    Floyd_Warshall_algorithm(vertices, edges)
    end_time = current_time_millis()
    
    floyd_sparse.append(round(end_time - start_time, 3))


# plot the obtained results
# Dijkstra and Floyd-Warshall separately
plot.figure()

plot.plot(input_sizes, dijkstra_dense, color="red", label="Dense graph")
plot.plot(input_sizes, dijkstra_sparse, color="blue", label="Sparse graph")

plot.title("Dijkstra Algorithm", color="violet", fontsize=16)
plot.legend(loc='upper left')

plot.xlabel("n", color="violet", fontsize=14)
plot.ylabel("T(millis)", color="violet", fontsize=14)

plot.grid()
plot.show()


plot.figure()

plot.plot(input_sizes, floyd_dense, color="red", label="Dense graph")
plot.plot(input_sizes, floyd_sparse, color="blue", label="Sparse graph")

plot.title("Floyd-Warshall Algorithm", color="violet", fontsize=16)
plot.legend(loc='upper left')

plot.xlabel("n", color="violet", fontsize=14)
plot.ylabel("T(millis)", color="violet", fontsize=14)

plot.grid()
plot.show()


# comparative analysis of Dijkstra and Floyd-Warshall algorithms
plot.figure()

plot.plot(input_sizes, dijkstra_dense, color="red", label="Dijkstra")
plot.plot(input_sizes, floyd_dense, color="blue", label="Floyd-Warshall")

plot.title("Dense graphs", color="violet", fontsize=16)
plot.legend(loc='upper left')

plot.xlabel("n", color="violet", fontsize=14)
plot.ylabel("T(millis)", color="violet", fontsize=14)

plot.grid()
plot.show()


plot.figure()

plot.plot(input_sizes, dijkstra_sparse, color="red", label="Dijkstra")
plot.plot(input_sizes, floyd_sparse, color="blue", label="Floyd-Warshall")

plot.title("Sparse graphs", color="violet", fontsize=16)
plot.legend(loc='upper left')

plot.xlabel("n", color="violet", fontsize=14)
plot.ylabel("T(millis)", color="violet", fontsize=14)

plot.grid()
plot.show()