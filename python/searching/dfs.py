def dfs(graph, start, visited=None):
    ''' Recursive depth-first search returning list of visited vertices '''
    if visited is None:
        visited = []

    visited.append(start)
    for vertex in graph[start]:
        if vertex in visited:
            continue
        else:
            dfs(graph, vertex, visited)

    return visited

