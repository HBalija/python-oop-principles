#!/usr/bin/python3


"""
Default behaviour of summing lists:
[1, 2, 3] + [4, 5, 6]
>> [1, 2, 3, 4, 5, 6]
"""


class CustomList:

    def __init__(self, this_list):
        self.mylist = this_list

    def __add__(self, other):
        """
        Takes SomeList object and adds it to another CustomList object by its
        index. Returns new SumList object.
        """
        new_list = [x + y for x, y in zip(self.mylist, other.mylist)]
        return CustomList(new_list)

    def __contains__(self, string):
        """
        Checks if a string or reversed string is in list.
        """
        return any(i in self.__str__() for i in [string, string[::-1]])

    def __str__(self):
        return str(self.mylist)


# add example

l1 = CustomList(list(range(1, 6)))
l2 = CustomList([100, 200, 300, 400, 500])

# calling add method --> cc.__add__(dd) using "+" operator
l3 = l1 + l2

# calling repr method --> ee__repr__()
print(l3)
# >> [101, 102, 103, 104, 105]


# contains example

string_list = CustomList(['abc'])

print('abc' in string_list)
# True

print('acb' in string_list)
# False

print('cba' in string_list)
# True --> would result False if our self.__contains__() wasn't called
