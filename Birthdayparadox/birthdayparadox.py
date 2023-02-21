import random
import datetime


def get_birthdays(number_of_birthdays):
    """ Возвращаем список объектов дат для случайных дней рождения."""
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 365))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """ Возвращаем объект даты дня рождения, встречающегося
    несколько раз в списке дней рождения."""
    if len(birthdays) == len(set(birthdays)):
        return None  # Все дни рождения различны, возвращаем None.

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Возвращаем найденные соответствия.


# Вводная информация:
print('''Парадокс дня рождения показывает нам, что в группе из N человек 
шансы на то, что у двоих из них совпадают дни рождения, на удивление велико.
Эта программа выполняет симуляцию Монте-Карло.
На самом деле это не парадокс, это просто неожиданный результат.''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Запрашиваем, пока пользователь не введет допустимое значение.
    print('Сколько дней рождений сгенерировать? (max 100) ')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numb_days = int(response)
        break
    else:
        print('Недопустимое значение')

print()

# Генерируем и отображаем дни рождения:
print(f'Here are {numb_days} birthdays:')
birthdays = get_birthdays(numb_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    data_text = '{} {}'.format(month_name, birthday.day)
    print(data_text, end='')

print()
print()

# Выясняем, встречаются ли два совпадающих дня рождения.
match = get_match(birthdays)
print('В этой симуляции, ', end='')
if match is not None:
    month_name = MONTHS[match.month - 1]
    data_text = '{} {}'.format(month_name, match.day)
    print('у нескольких людей день рождение', data_text)
else:
    print('нет одинаковый дней рождений')
print()

# Производим 100 000 операций имитационного моделирования:
print(f'Генерация {numb_days} случайных дней рождений 100.000 раз...')
input('Нажмите Enter чтобы начать')

print('Давайте проведем еще 100.000 симуляций.')
sim_match = 0  # Число операций моделирования с совпадающими днями рождения.

for i in range(100_000):
    # Отображаем сообщение о ходе выполнения каждые 10 000 операций:
    if i % 10_000 == 0:
        if i == 0:
            print('simulations run...')
        else:
            print(f'{i} simulations run...')

    birthdays = get_birthdays(numb_days)
    if get_match(birthdays) is not None:
        sim_match = sim_match + 1
print('100.000 simulations run.')

# Отображаем результаты имитационного моделирования:
probability = round(sim_match / 100_000 * 100, 2)
print(f'Out of 100,000 simulations of {numb_days}, people, there was a')
print(f'matching birthday in that group, {sim_match}, times. This means')
print(f'that, {numb_days}, people have a, {probability} % chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')