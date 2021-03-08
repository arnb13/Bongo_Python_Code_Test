import unittest
import solution3

class TestSolution3(unittest.TestCase):
    def test_lca(self):
        result = solution3.lca(6, 7)
        self.assertEqual(result, 3)

        result = solution3.lca(3, 7)
        self.assertEqual(result, 3)

        result = solution3.lca(4, 7)
        self.assertEqual(result, 1)

        result = solution3.lca(5, 2)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
