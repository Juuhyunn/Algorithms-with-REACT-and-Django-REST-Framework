from dataclasses import dataclass
from builtins import property

from django.db import models

# Create your models here.


class Sorting(object):
    def bubble_sort(self):
        pass

    def merge_sort(self):
        pass

    def quick_sort(self):
        pass

@dataclass
class Palindrome(object):
    input_string : str

    @property
    def input_string(self) -> str: return self._input_string
    @input_string.setter
    def input_string(self, input_string): self._input_string = input_string


    def str_to_list(self) -> []:
        return [i.lower() for i in self.input_string if i.isalnum()]

    def isPalindrome(self, ls : []) -> bool:
        return {False for i in ls if ls.pop(0) != ls.pop()}

    def reverse_string(self, ls : []) -> []:
        # return ls[::-1]
        return [ls.pop() for i in range(len(ls))]


@dataclass
class MySum(object):
    start_number: int
    end_number: int

    @property
    def start_number(self) -> int : return self._start_number

    @start_number.setter
    def start_number(self, start_number): self._start_number = start_number

    @property
    def end_number(self) -> int : return self._end_number

    @end_number.setter
    def end_number(self, end_number): self._end_number = end_number


    # example 1
    def one_to_ten_sum_1(self):
        sum = 0
        for i in range(self.start_number, self.end_number):
            sum += i
        return sum

    # example 2
    def one_to_ten_sum_2(self):
        return sum(i for i in range(self.start_number, self.end_number))

    # example 3
    def one_to_ten_sum_3(self):
        return sum(range(self.start_number, self.end_number))
