"""
    迭代器 >>>
"""


class MyRange:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return MyRangeIterator(self.number)

"""
class MyRangeIterator:
    def __init__(self, end_value):
        self.end_value = end_value
        self.__number = 0

    def __next__(self):
        if self.__number == self.end_value:
            raise StopIteration
        temp = self.__number
        self.__number += 1
        return temp
"""

for item in MyRange(-1):
    print(item)
