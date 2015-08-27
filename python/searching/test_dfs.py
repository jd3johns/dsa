import unittest

from dfs import dfs

class TestDFS(unittest.TestCase):
    '''
    Test cases:
        Connected graph
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
        out_visited = ['A', 'B', 'F', 'D', 'C', 'E']

        self.assertEqual(dfs(graph, start), out_visited)
