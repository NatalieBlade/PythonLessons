import unittest
from calc import calculator


class TestCount(unittest.TestCase):
    def test_res(self):
        res = calculator(5, 5, "*")
        self.assertEqual(res, 25)


if __name__ == "__name__":
    unittest.main()