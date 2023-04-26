import sys

def Dijkstra_algorithm(vertices, edges, source):
    
    def to_be_visited():
        v = -10
        for index in range(num_of_vertices):
            if (visited_and_distance[index][0] == 0) and (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
                v = index
        return v

    num_of_vertices = len(vertices[0])

    visited_and_distance = list()
    for i in range(num_of_vertices):
        if i == source:
             visited_and_distance.append([0, 0])
        else:
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


def Floyd_Warshall_algorithm(vertices, edges):
    num_of_vertices = len(vertices[0])
    distance = edges

    for k in range(num_of_vertices):
        for i in range(num_of_vertices):
            for j in range(num_of_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

def normalizeVerticesSet (n_vertices, vertices, edges):
    for x in range(n_vertices - 1):
        for y in range(n_vertices - 1):
            if (vertices[x][y] == 0) and (x != y):
                edges[x][y] = sys.maxsize


vertices = [[0, 1, 1, 0],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 0]]

edges = [[0, 4, 1, 0],
         [4, 0, 3, 2],
         [1, 3, 0, 4],
         [0, 2, 4, 0]]


for source in range(4):
    result = Dijkstra_algorithm(vertices, edges, source)
    print(result)

normalizeVerticesSet(5, vertices, edges)
print(Floyd_Warshall_algorithm(vertices, edges))