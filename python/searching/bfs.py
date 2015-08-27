def bfs(graph, start):
    '''
    Breadth-first search using an array as a queue, returning list of
    visited vertices.
    '''
    queue = [start]
    visited = []

    while len(queue) != 0:
        vertex = queue.pop(0)
        visited.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)

    return visited

