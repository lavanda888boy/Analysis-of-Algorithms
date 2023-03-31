from time import time


# Breadth-First Search algorithm
def bfs(graph, root, search_set, counter):

    visited, queue = set(), list()
    queue.append(root)
    visited.add(root)

    while queue:
        if counter == 5:
            return

        vertex = queue.pop(0)
        
        if vertex in search_set:
            counter += 1

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Depth-First Search algorithm
def dfs(graph, start, search_set, counter, visited=None):
    if counter == 5:
        return
    
    if start in search_set:
        counter += 1

    if visited is None:
        visited = list()
    visited.append(start)

    for next in graph[start] - set(visited):
        dfs(graph, next, visited, counter)

    return visited


def current_time_nanos():
    return time() * 1000000


# setting up input data
unbalanced_tree = {0: set([1, 2]), 1: set([3, 4, 5, 11, 12]), 2: set([6, 7]), 3: set([]), 4: set([]),
                   5: set([]), 6: set([8, 9, 10]), 7: set([]), 8: set([]), 9: set([]), 10: set([14]),
                   11: set([]), 12: set([13, 17]), 13: set([15, 16]), 14: set([])}

unbalanced_dfs_set = set([5, 6, 14, 16, 17])
unbalanced_bfs_set = set([2, 4, 7, 8, 12])

balanced_tree = {0: set([1, 2, 3]), 1: set([4, 5]), 2: set([6, 7]), 3: set([8, 16]), 4: set([]),
                 5: set([9, 10, 11]), 6: set([]), 7: set([12, 13]), 8: set([14, 15]), 9: set([]), 10: set([]),
                 11: set([]), 12: set([]), 13: set([]), 14: set([]), 15: set([]), 16: set([])}

balanced_dfs_set = set([3, 7, 9, 15, 16])
balanced_bfs_set = set([4, 6, 8, 11, 16])

c = 0
start_time = current_time_nanos()
dfs(balanced_tree, 0, balanced_dfs_set, c)
end_time = current_time_nanos()
print(end_time - start_time)
