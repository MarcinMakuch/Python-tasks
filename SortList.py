import typing

def sort_list(my_list: typing.List[int]):
    return my_list.sort()



assert sort_list([3, 1, 3, 2]) == [1, 2, 3, 3]
assert sort_list([0, 0, 0]) == [0, 0, 0]
assert sort_list([10, 9, 8, -10, -20, -30]) == [-30, -20, -10, 8, 9, 10]
print('ok')