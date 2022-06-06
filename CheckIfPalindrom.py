def check_if_palindrom(word: str):
    reversed_word = word[::-1]
    if word.__eq__(reversed_word):
        return True
    return False


assert check_if_palindrom('oko') == True
assert check_if_palindrom('mama') == False
assert check_if_palindrom('potop') == True
print('ok')
