import unittest

from bfs import bfs

class TestBFS(unittest.TestCase):
    '''
    Test cases:
        Connected graph: regular graph
        Cyclical graph: A -> B -> A
    '''

    def test_connected_graph(self):
        graph = {'A': ['B', 'C'],
                 'B': ['F', 'D'],
                 'C': ['D', 'E'],
                 'D': [],
                 'E': [],
                 'F': []
                }
        start = 'A'
        out_visited = ['A', 'B', 'C', 'F', 'D', 'E']

        self.assertEqual(bfs(graph, start), out_visited)

    def test_cyclical_graph(self):
        graph = {'A': ['B', 'C', 'D'],
                 'B': ['E', 'A'],
                 'C': ['E', 'A'],
                 'D': ['E', 'A'],
                 'E': []
                }
        start = 'A'
        out_visited = ['A', 'B', 'C', 'D', 'E']

        self.assertEqual(bfs(graph, start), out_visited)
