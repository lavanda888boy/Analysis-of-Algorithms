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
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


if __name__ == '__main__':
    graph = {0: set([1, 2]), 1: set([2]), 2: set([3]), 3: set([1, 2])}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
    print(dfs(graph, 0))