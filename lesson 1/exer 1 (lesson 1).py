# Задание 1
# Написать программу, считывающую одно число из строки, которая должна выводить:
# a. Если число положительное - "Положительное"
# b. Если число отрицательное - "Отрицательное"
# c. Если число это ноль - "Ноль
# вход - одно число
# выход - строка


number = int(input('Введите число: '))
if number > 0:
    print(number, '- положительное')
elif number < 0:
    print(number, '- отрицательное')
else:
    print(number, '- ноль')
