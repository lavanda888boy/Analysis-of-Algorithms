from time import time


# Breadth-First Search algorithm
def bfs(graph, root):

    visited, queue = set(), list()
    queue.append(root)
    visited.add(root)

    while queue:

        vertex = queue.pop(0)
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Depth-First Search algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = list()
    visited.append(start)

    for next in graph[start] - set(visited):
        dfs(graph, next, visited)

    return visited


def current_time_nanos():
    return time() * 1000000


unbalanced_tree = {0: set([1, 2]), 1: set([3, 4, 5, 11, 12]), 2: set([6, 7]), 3: set([]), 4: set([]),
                   5: set([]), 6: set([8, 9, 10]), 7: set([]), 8: set([]), 9: set([]), 10: set([14]),
                   11: set([]), 12: set([13, 17]), 13: set([15, 16]), 14: set([])}

balanced_tree = {0: set([1, 2, 3]), 1: set([4, 5]), 2: set([6, 7]), 3: set([8, 16]), 4: set([]),
                 5: set([9, 10, 11]), 6: set([]), 7: set([12, 13]), 8: set([14, 15]), 9: set([]), 10: set([]),
                 11: set([]), 12: set([]), 13: set([]), 14: set([]), 15: set([]), 16: set([])}

