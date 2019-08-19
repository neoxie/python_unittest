import unittest
from sorts import *


# inherit unittest.TestCase
class TestSorts(unittest.TestCase):

    # start with test and append testing method name
    def test_normal_sort(self):
        arr = [3, 4, 1, 5, 6]
        normal_sort(arr)
        # assert the result
        self.assertEqual(arr, [1, 3, 4, 5, 6])

    def test_bubble_sort(self):
        arr = [3, 4, 1, 5, 6]
        bubble_sort(arr)
        # assert
        self.assertEqual(arr, [1, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
