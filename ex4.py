def compare_two_numbers(a: int, b: int):
    if a < b:
        result = f"{a} is smaller than {b}"
    elif a > b:
        result = f"{a} is greater than {b}"
    else:
        result = f"a is equal b: 0"
    return result

assert compare_two_numbers(2, 6) == '2 is smaller than 6'
assert compare_two_numbers(4, -5) == '4 is greater than -5'
assert compare_two_numbers(100, 100) == 'a is equal b: 0'
print('ok')
