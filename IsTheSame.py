from typing import List


def is_the_same(my_list: List[any]):
    first_el = my_list[0]
    for element in my_list:
        if element != first_el:
            return False
    return True


assert is_the_same([1, 1, 1]) == True
assert is_the_same([1, 2, 1]) == False
assert is_the_same([True]) == True
assert is_the_same(['blue', 'blue']) == True
assert is_the_same([2, 'red']) == False
print('ok')
