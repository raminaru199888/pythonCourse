# Задача 1.
# На вход поступает три числа через пробел

# Output
# Вывод - два числа, если дискриминант положительный
# Одно число (или два одинаковых, по желанию) если дискриминант отрицательный
# "Нет корней", если дискриминант меньше нуля
# Примеры ввода

# Пример 1
# Input:
# 1 3 -4

# Output:
# -4 1

# Пример 2
# Input:
# 1 -2 1

# Output:
# 1

# Пример 3
# Input:
# 1 2 4

# Output:
# Нет корней

import math
def quadratic_equation(a, b, c):
    D = b**2 - 4 * a * c  # Квадратное уравнение

    if D == 0:  # 1 корень имеет
        x = -b / 2 * a
        return int(x)
    if D > 0:  # 2 различных корня имеет
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        return int(x1), int(x2)
    if D < 0:  # корней нет
        return 'Нет корней'

number = input("Введите коэффициенты для квадратного уравнения, в формате: a b c ").split(' ')
a = int(number[0])
b = int(number[1])
c = int(number[2])
print(quadratic_equation(a, b, c))



