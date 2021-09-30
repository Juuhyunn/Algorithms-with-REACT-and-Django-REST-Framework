from django.test import TestCase
import unittest
# Create your tests here.
# import sys
# sys.path.append('/admin/sorting')
from models import MySum, Palindrome

class TestMySum(unittest.TestCase):
    def test_one_to_ten_sum_1(self):
        instance = MySum()
        instance.start_number = 1
        instance.end_number = 11
        res = instance.one_to_ten_sum_1()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)

class TestPalindrome(unittest.TestCase):

    def test_str_to_list(self):
        instance = Palindrome()
        instance.input_string = 'applyyrthE'
        ls = instance.str_to_list()
        print(f'My Expected Value is {ls}')
        res = instance.isPalindrome(ls)
        print(f'My Expected Value is {res}')
        self.assertEqual(res, {False})

    def test_reverse_string(self):
        instance = Palindrome()
        instance.input_string = 'applE'
        ls = instance.str_to_list()
        print(f'My Expected Value is {ls}')
        res = instance.reverse_string(ls)
        self.assertEqual(res, ['e', 'l', 'p', 'p', 'a'])



if __name__ == '__main__':
    unittest.main()
