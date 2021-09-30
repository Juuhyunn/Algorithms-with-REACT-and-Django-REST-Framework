from dataclasses import dataclass

@dataclass
class Sorting(object):
    random_arr: []

    @property
    def random_arr(self): return self._random_arr
    @random_arr.setter
    def random_arr(self, random_arr): self._random_arr = random_arr

    def bubble_sort(self) -> []:
        arr = self._random_arr
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def merge_sort(param: []) -> []:
        pass

    @staticmethod
    def quick_sort(param: []) -> []:
        pass