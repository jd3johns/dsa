import unittest

from dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    ''' Test Dijkstra's single-source shortest-paths finding algorithm '''

    def test_standard_case(self):
        '''
        Test a standard, successful case of the algorithm
        by using an example from T. Cormen's "Introduction to
        Algorithms" text, part 24.3.
        '''
        # input
        graph = {'s': {'t': 10, 'y': 5},
                 't': {'y': 2, 'x': 1},
                 'x': {'z': 4},
                 'y': {'t': 3, 'x': 9, 'z': 2},
                 'z': {'s': 7, 'x': 6}
                }
        source = 's'

        # output
        out_distances = {'s': 0, 't': 8, 'x': 9, 'y': 5, 'z': 7}
        out_predecessors = {'s': None, 't': 'y', 'x': 't', 'y': 's', 'z': 'y'}

        # run the test
        distances, predecessors = dijkstra(graph, source)
        self.assertEqual(distances, out_distances)
        self.assertEqual(predecessors, out_predecessors)

                 
