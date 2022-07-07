# Задание 2
# Написать программу, считывающую номер месяца (от 1 до 12) и выводящая количество дней в месяце
# Если месяц - февраль, выводить строку "ФЕВРАЛЬ!"
# вход - одно число
# выход - одно число или строка "ФЕВРАЛЬ!"

numberMonth = ''
while numberMonth != 0:
    numberMonth = int(input('Введите целое число: '))
    if numberMonth >= 13:
        print("Ошибка! Введите целое число от 1 до 12!")
        break
    month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    if numberMonth == 1 or numberMonth == 3 or numberMonth == 5 or numberMonth == 7 or numberMonth == 8 or numberMonth == 10 or numberMonth == 12:
        print('В', month[numberMonth % 12 - 1], '31 дней')
    elif numberMonth == 4 or numberMonth == 6 or numberMonth == 9 or numberMonth == 11:
        print('В', month[numberMonth % 12 - 1], '30 дней')
    elif numberMonth == 2:
        print('В', month[numberMonth % 12 - 1], '28 дней')
