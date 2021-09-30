import unittest
from models_sort import Sorting

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self) -> []:
        instance = Sorting()
        instance.random_arr = [6, 3, 4, 5, 2, 1]
        self.assertEqual(instance.bubble_sort(), [1, 2, 3, 4, 5, 6])


    def test_merge_sort(param: []) -> []:
        pass

    def test_quick_sort(param: []) -> []:
        pass