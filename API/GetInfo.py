from collections import Counter

import requests
from bs4 import BeautifulSoup as soup

url = 'https://pl.wikipedia.org/wiki/Iga_%C5%9Awi%C4%85tek'


def count_vovels(data: str) -> int:
    vowel_number = 0
    for letter in data:
        if letter in ('a', 'e', 'o', 'u', 'i', 'y'):
            vowel_number += 1
    return vowel_number


def letter_count(text):
    return Counter(c for c in text.lower() if c.isalpha())


def get_statistics(url: str) -> dict:
    response = requests.get(url)
    if response.status_code != 200:
        print('nie otrzymano odpowiedzi')
        return
    html_data = soup(response.text, 'html.parser')

    word_counter = 0
    vowels_counter = 0
    letter_counter = dict()

    for a in html_data.findAll("a"):
        text = a.text
        number_of_words = len(text.split(" "))
        word_counter += number_of_words
        number_of_vowels = count_vovels(text)
        vowels_counter += number_of_vowels
        dict_of_letteres = letter_count(text)
        for letter, value in dict_of_letteres.items():
            if letter_counter.get(letter, None):
                letter_counter[letter] += value
            else:
                letter_counter[letter] = value

    most_frequent_letter = max(letter_counter, key=letter_counter.get)
    return {
        'number of words': word_counter,
        'vowels counter': vowels_counter,
        'most freq letter': f"most freq letter is {most_frequent_letter} : {letter_counter[most_frequent_letter]}",
        'number of a': len(html_data.find_all("a"))
    }


print(get_statistics(url))
