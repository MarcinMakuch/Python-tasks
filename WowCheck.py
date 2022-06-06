def wow(number: int):
    return "W" + number * 'o' + "w"


assert wow(1) == 'Wow'
assert wow(4) == 'Woooow'
assert wow(0) == 'Ww'
print('ok')

