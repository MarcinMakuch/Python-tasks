def check_pattern(sentence: str, pattern: str):
    if sentence.__contains__(pattern):
        return 'YES'
    return 'NO'


assert check_pattern('AABBABA', 'BBAA') == 'NO'
assert check_pattern('AAABBB', 'BBBAAA') == 'NO'
assert check_pattern('AABB', 'ABB') == 'YES'
print('ok')
