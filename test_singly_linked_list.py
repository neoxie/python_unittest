import unittest
from singly_linked_list import *


# inherit unittest.TestCase
class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.sll = SinglyLinkedList()
        self.sll.convert_array_to_list(arr)

    # start with test and append testing method name
    def test_convert_to_array(self):
        new_arr = self.sll.convert_to_array()
        # assert the result
        self.assertEqual(new_arr, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_insert_to_head(self):
        self.sll.insert_to_head(2)
        new_arr = self.sll.convert_to_array()
        # assert the result
        self.assertEqual(new_arr, [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_find_by_value(self):
        value = 1
        found_node = self.sll.find_by_value(value)
        self.assertEqual(value, found_node.data)

    def test_find_by_index(self):
        index = 5
        found_node = self.sll.find_by_index(index)
        self.assertEqual(6, found_node.data)

    def test_delete_by_node(self):
        value = 1
        found_node = self.sll.find_by_value(value)
        self.sll.delete_by_node(found_node)
        new_arr = self.sll.convert_to_array()
        self.assertEqual(new_arr, [2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_delete_by_value(self):
        value = 10
        found_node = self.sll.find_by_value(value)
        self.sll.delete_by_node(found_node)
        new_arr = self.sll.convert_to_array()
        self.assertEqual(new_arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_reversed_self(self):
        self.sll.reversed_self()
        new_arr = self.sll.convert_to_array()
        self.assertEqual(new_arr, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
