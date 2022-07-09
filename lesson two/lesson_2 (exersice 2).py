# На входе список из чисел, каждое число повторяется два раза,
# и только одно число повторяется 1 раз. Найти число, которое повторяется 1 раз.


number = input('Введите числа: ').split()
list_number = []
for i in range(len(number)):
    list_number.append(number[i])
for k in list_number:
    if list_number.count(k) == 1:
        print('Не повторяющееся число: ', k)


