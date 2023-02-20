import random

NUM_DIGITS: int = 3
MAX_GUESSES: int = 10
COLOR_TEXT = '\u001b[32;1m'


def main():
    print(COLOR_TEXT)
    print('''Я загадал {}-значное число без повторяющихся цифр.
    
Попробуйте его угадать. Вот несколько подсказок:
Когда я говорю: |  Это означает:
----------------+---------------------------------------------------------------
    Pico        |  Одна цифра правильная, но находится в неправильном положении.
    Fermi       |  Одна цифра верна и находится в правильном положении.
    Bagels      |  Ни одна цифра не является правильной.

Например, если секретное число было 248, а ваше предположение - 843, то
подсказка была бы: Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        secret_num: str = get_secret_num()
        print(f'Я придумал число из {NUM_DIGITS} чисел \n'
              f'У вас {MAX_GUESSES} попыток')

        number_of_guesses: int = 1
        while number_of_guesses <= MAX_GUESSES:
            guess: str = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Попытка #{number_of_guesses}')
                guess = input('> ')

            hint: str = get_hint(guess, secret_num)
            print(hint)
            number_of_guesses += 1

            if guess == secret_num:
                break
            if number_of_guesses > MAX_GUESSES:
                print('У вас закончились попытки \n'
                      f'Ответ был {secret_num}')

        print('Хотим ли ещё сыграть (y/n))')
        if not input('> ').lower().startswith('y'):
            break
    print('Спасибо за игру')


def get_secret_num():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers: list = list('0123456789')
    random.shuffle(numbers)
    secret_num: str = ''
    for index in range(NUM_DIGITS):
        secret_num += str(numbers[index])
    return secret_num


def get_hint(guess, secret_num):
    """Возвращает строку с подсказками pico, fermi, bagels """
    if guess == secret_num:
        return "You're Goddamn Right"

    hint = []

    for index in range(len(guess)):
        if guess[index] == secret_num[index]:
            hint.append('Fermi')
        elif guess[index] in secret_num:
            hint.append('Pico')
    if len(hint) == 0:
        return 'Bagels'
    else:
        hint.sort()
        return ' '.join(hint)


if __name__ == '__main__':
    main()
