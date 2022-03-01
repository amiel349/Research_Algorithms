import unittest
import math
import io
import sys

from EX1 import Q1, Q2, Q3


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
    def test_q2(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        Q2.print_sorted({"a":5, "c":6, "b":[1, 3, 2, 4]})
        output = new_stdout.getvalue()
        output=output.rstrip("\n")


        self.assertEqual(output,"{'a': 5, 'b': [1, 2, 3, 4], 'c': 6}")
        sys.stdout = old_stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        Q2.print_sorted({6: 5, -3: 6, 4: ("a", "z", "d", "g", "h")})
        output2 = new_stdout.getvalue()
        output2 = output2.rstrip("\n")

        self.assertEqual( output2,"{-3: 6, 4: ['a', 'd', 'g', 'h', 'z'], 6: 5}")
        sys.stdout = old_stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        Q2.print_sorted([[8, 3, 9, 4], [{1: 5, -8: 5, 7: 4}]])
        output3 = new_stdout.getvalue()
        output3 = output3.split('\n', 1)[1]
        output3 = output3.rstrip("\n")
        self.assertEqual(output3,"[[3, 4, 8, 9], [{-8: 5, 1: 5, 7: 4}]]")
        sys.stdout = old_stdout

    def test_q3(self):
        #assert true
        assert Q3.find_root(lambda x: (x - 4) * (x + 2), 2, 5) - 4 < 0.000001
        assert Q3.find_root(lambda x: x ** 2 - 7, 2, 5) - 2.6457513456 < 0.000001
        assert Q3.find_root(lambda x: x ** 3 - 50 * x - 500, 2, 15) - 10 < 0.000001
        assert Q3.find_root(lambda x: x ** 4 - x ** 3 - x ** 2 - x, 2, 8) - 1.8392867552270147 < 0.000001
        assert Q3.find_root(lambda x: math.log2(x) - 3, 2, 10) - 8 < 0.000001
        assert Q3.find_root(lambda x: math.exp(math.log(x, math.exp(1))) - 10, 2, 10) - 10 < 0.000001
        # assert false- same tests now with wrong answer
        self.assertFalse((Q3.find_root(lambda x: (x - 4) * (x + 2), 2, 5) - 3 < 0.000001))
        self.assertFalse(Q3.find_root(lambda x: x ** 2 - 7, 2, 5) - 1 < 0.000001)
        self.assertFalse(Q3.find_root(lambda x: x ** 3 - 50 * x - 500, 2, 15) - 9 < 0.000001)
        self.assertFalse(Q3.find_root(lambda x: x ** 4 - x ** 3 - x ** 2 - x, 2, 8) - 1 < 0.000001)
        self.assertFalse(Q3.find_root(lambda x: math.log2(x) - 3, 2, 10) - 7 < 0.000001)
        self.assertFalse(Q3.find_root(lambda x: math.exp(math.log(x, math.exp(1))) - 10, 2, 10) - 9 < 0.000001)




if __name__ == '__main__':
    unittest.main()
