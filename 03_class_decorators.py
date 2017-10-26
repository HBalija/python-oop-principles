#!/usr/bin/python3

from random import randint


class MaxSizeList:
    """
    Creates a list with size defined by argument. Also sets id for instance and
    instance counter.
    """
    _counter = 0

    def __init__(self, max_size):

        self.max_size = MaxSizeList.set_max_size(max_size)
        self._value = []
        MaxSizeList._counter += 1
        self.id = MaxSizeList._counter

    @classmethod
    def get_counter(cls):
        return cls._counter

    @staticmethod
    def set_max_size(size):
        try:
            return abs(int(size))
        except ValueError:
            return randint(1, 6)

    def push(self, value):
        self._value.append(value)
        if len(self._value) > self.max_size:
            self._value.pop(0)

    @property
    def list(self):
        return self._value


# example

a = MaxSizeList(3)
b = MaxSizeList(1)

print(MaxSizeList.get_counter())

c = MaxSizeList('string')

a.push('hey')
a.push('hi')
a.push('let\'s')
a.push('go')

b.push('hey')
b.push('hi')
b.push('let\'s')
b.push('go')

c.push('hey')
c.push('hi')
c.push('let\'s')
c.push('go')

print(a.list)
print(b.list)
print(c.list)


"""
2
['hi', "let's", 'go']
['go']
random list
"""
