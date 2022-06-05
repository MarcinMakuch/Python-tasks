def read_words_vowels_spaces(path):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    counter_vowels = 0
    counter_spaces = 0
    with open(path, 'rt') as file:
        data = file.read()
    words_count = len(data.split(" "))
    for single_sign in data:
        if single_sign in vowels:
            counter_vowels += 1
        if single_sign == " ":
            counter_spaces += 1
    return f"Ilość słów to {words_count}, ilość samogłosek to {counter_vowels}, ilość spacji to {counter_spaces}"


print(read_words_vowels_spaces('sample.txt'))
