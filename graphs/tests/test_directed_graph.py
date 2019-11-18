import unittest
from graph.directed_graph.directed_graph import DirectedGraph


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.vertices = {0: [1], 1: [2, 3], 2: [3], 3: [4, 6], 4: [5, 6], 5: [5], 6: [6]}
        self.directed_graph = DirectedGraph(self.vertices)

    def test_init(self):
        self.assertEqual(len(self.vertices.keys()), self.directed_graph.get_vertices_count())

    def test_add_vertex(self):
        label = 7
        self.directed_graph.add_vertex(label)
        vertex = self.directed_graph.get_vertex(label)
        self.assertIsNotNone(vertex)
        self.assertEqual(vertex.get_outdegree(), 0)
        self.assertEqual(vertex.get_indegree(), 0)
        self.assertSetEqual(vertex.get_tails(), set())

    def test_add_duplicate_vertex(self):
        label = 7
        self.directed_graph.add_vertex(label)
        with self.assertRaises(RuntimeError): 
            self.directed_graph.add_vertex(label)

    def test_add_tails(self):
        vertex_to_test = 7
        self.directed_graph.add_vertex(vertex_to_test)
        vertex = self.directed_graph.get_vertex(vertex_to_test)
        no_tails = 3
        for i in range(no_tails):
            vertex.add_tail(i)
        self.assertEqual(len(vertex.get_tails()), no_tails)
        self.assertEqual(vertex.get_outdegree(), len(vertex.get_tails()))        

    def test_outdegree(self):
        vertex = self.directed_graph.get_vertex(1)
        self.assertEqual(vertex.get_outdegree(), len(vertex.get_tails()))

    def test_indegree(self):
        vertex_to_test = 6
        self.vertices = {0: [1], 1: [2, 3], 2: [3], 3: [4, vertex_to_test], 4: [5, vertex_to_test], 5: [5], vertex_to_test: []}
        self.directed_graph = DirectedGraph(self.vertices)
        vertex = self.directed_graph.get_vertex(vertex_to_test)
        self.assertEqual(vertex.get_indegree(), 2)

    def test_create_SCCs(self):
        self.vertices = {0: [1], 1: [2, 3], 2: [3], 3: [4], 4: [5, 2], 5: [6], 6: [7], 7 : [5]}
        self.directed_graph = DirectedGraph(self.vertices)
        sccs = self.directed_graph.create_SCCs()
        ok = False
        ok_234 = False
        ok_567 = False
        ok_0 = False
        ok_1 = False
        for key, vertices in sccs.items():
            sorted_vertices = sorted(list(vertices))
            if sorted_vertices == [2, 3, 4]:
                ok_234 = True
            elif sorted_vertices == [5, 6, 7]:
                ok_567 = True
            elif sorted_vertices == [1]:
                ok_1 = True
            elif sorted_vertices == [0]:
                ok_0 = True
        self.assertTrue(ok_234 == True and ok_567 == True and ok_0 == True and ok_1 == True)


if __name__ == '__main__':
    unittest.main()
