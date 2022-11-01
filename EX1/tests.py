import unittest
import io
import sys
from EX1 import Q1, Q2, Q3

graph = {
    "a": ["b", "c"],  # a-----------b
    "b": ["a", "d"],  # |           |
    "c": ["a", "d"],  # |           |
    "d": ["e"],       # c-----------d-----------e
    "e": ["d"]
}


def four_neighbor_function(node) -> list:
    (x, y) = node
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def alphabet_neighbor_function(node) -> list:
    return [chr(ord(node) + 1), chr(ord(node) - 1)]


def graph_neighbor_function(node) -> list:
    if node in graph.keys():
        return graph[node]


def f1(x: int, y: float, z):
    return x * y * z


def f2(x: int, y: float, z):
    return x - y - z


def f3(x: str, y: str, z):
    return x + y + z


class MyTestCase(unittest.TestCase):

    def test_q1(self):
        assert 8 == Q1.safe_call(f1, x=2, y=2.0, z=2)
        assert -8 == Q1.safe_call(f1, x=2, y=2.0, z=-2)
        assert "abc" == Q1.safe_call(f3, x="a", y="b", z="c")
        assert 0 == Q1.safe_call(f2, x=10, y=5.0, z=5)
        assert 2 == Q1.safe_call(f2, x=-2, y=-2.0, z=-2)
        with self.assertRaises(Exception) as error:
            Q1.safe_call(f1, x=2.0, y=2.0, z=2)
            assert "The variables doesnt match" in error
        with self.assertRaises(Exception) as error:
            Q1.safe_call(f2, x=2, y=2, z=2)
            assert "The variables doesnt match" in error
        with self.assertRaises(Exception) as error:
            Q1.safe_call(f3, x=2, y="abc", z=2)
            assert "The variables doesnt match" in error

    def test_q3(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        Q3.print_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})
        output = new_stdout.getvalue()
        output = output.rstrip("\n")

        self.assertEqual(output,"{'a': 5, 'b': [1, 2, 3, 4], 'c': 6}")
        sys.stdout = old_stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        Q3.print_sorted({6: 5, -3: 6, 4: ("a", "z", "d", "g", "h")})
        output2 = new_stdout.getvalue()
        output2 = output2.rstrip("\n")

        self.assertEqual(output2, "{-3: 6, 4: ['a', 'd', 'g', 'h', 'z'], 6: 5}")
        sys.stdout = old_stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        Q3.print_sorted([[8, 3, 9, 4], [{1: 5, -8: 5, 7: 4}]])
        output3 = new_stdout.getvalue()
        output3 = output3.split('\n', 1)[1]
        output3 = output3.rstrip("\n")
        self.assertEqual(output3, "[[3, 4, 8, 9], [{-8: 5, 1: 5, 7: 4}]]")
        sys.stdout = old_stdout

    def test_q2(self):

        self.assertEqual(Q2.breadth_first_search((0, 0), (2, 2), four_neighbor_function),
                         "(0, 0) -> (1, 0) -> (2, 0) -> (2, 1) -> (2, 2)")
        self.assertEqual(Q2.breadth_first_search('a', 'e', alphabet_neighbor_function),
                         "a -> b -> c -> d -> e")
        self.assertEqual(Q2.breadth_first_search('e', 'a', alphabet_neighbor_function),
                         "e -> d -> c -> b -> a")
        self.assertEqual(Q2.breadth_first_search('a', 'e', graph_neighbor_function),
                         "a -> b -> d -> e")
        self.assertEqual(Q2.breadth_first_search('c', 'b', graph_neighbor_function),
                         "c -> a -> b")
        self.assertEqual(Q2.breadth_first_search('a', 'f', graph_neighbor_function),
                         "There is no path between 'a' and 'f'")


if __name__ == '__main__':
    unittest.main()
