from typing import List, Tuple


def sort_list(my_list: List[Tuple]):
    result = sorted(my_list, key = lambda x: x[1])
    return result


assert sort_list([('Ania', 20), ('Monika', 110), ('Piotr', 10)]) == [('Piotr', 10), ('Ania', 20), ('Monika', 110)]
assert sort_list([('Ania', -10), ('Monika', -110), ('Piotr', 210)]) == [('Monika', -110), ('Ania', -10), ('Piotr', 210)]
