from heapq import heappop, heappush

def dijkstra(graph, source):
    '''
    Find the single-source shortest-paths using Dijkstra's algorithm.

    Arguments:
        graph: Adjacency list describing graph with nonnegative edge weights.
               Dictionary of dictionaries of form {'a': {'b': 3, 'c': 2} ...}
               such that graph[u][v] gives edge length between edges u and v.
        source: Vertex from which shortest paths are to be discovered.
    '''
    # Initialize the single-source vertex distances
    distances = dict()
    predecessors = dict()
    for vertex in graph:
        distances[vertex] = float("inf")
        predecessors[vertex] = None
    distances[source] = 0

    # Initialize priority queue
    priority_q = [(0, source)]

    while priority_q:
        # Pull smallest vertex distance from queue
        path_len, current = heappop(priority_q)
        for vertex in graph[current]:
            # Relaxation of distance estimates
            if distances[vertex] > path_len + graph[current][vertex]:
                distances[vertex] = path_len + graph[current][vertex]
                predecessors[vertex] = current
                heappush(priority_q, (distances[vertex], vertex))

    return distances, predecessors
