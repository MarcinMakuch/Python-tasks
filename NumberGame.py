import random

random_num = random.randint(1, 51)
counter = 0

print('Zgadnij liczbę z zakresu 1- 50.')

while True:
    try:
        guess_num = int(input('Podaj liczbę: \n'))
    except ValueError as e:
        print('Podana wartość nie jest liczbą, podaj liczbę z zakresu 1-50.')
        continue
    counter += 1
    if guess_num == random_num:
        print(f"Wygrałeś w {counter} próbach.")
        new_game = input('Czy chcesz zagarać jeszcze raz? Wpisz Y dla nowej gry, N jeśli chcesz zakończyć.\n')
        if new_game == 'Y':
            counter = 0
            random_num = random.randint(1, 51)
            continue
        else:
            break
    if guess_num > random_num:
        print('Twoja liczba jest za duża, podaj inną liczbę.')
        continue
    else:
        print('Twoje liczba jest za mała, podaj inną liczbę.')
        continue

print('Koniec programu.')
