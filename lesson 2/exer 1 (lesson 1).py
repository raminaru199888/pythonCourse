
numbers = input('Введите целые числа: ',).split()
commonList = []
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    commonList.append(numbers[i])
print('Максимальный элемент: ', max(commonList))
print('Минимальный элемент: ', min(commonList), '\n')
for k in commonList:
    if k % 3 == 0:
        print('Число делящееся на три: ', k)
    else:
        print('Ошибка! Число', k, 'не делится на три!')
# возник вопрос, как вывести красиво все значения "Числа делящиеся на 3: <перечисление>? в одну строку, а не каждый раз с новой строки из-за циклв.
# Для этого создать пустой список и повторить добавление? или с помощью insert()
print()  # тут также плохо  с разделением \n'   :(
for i in commonList:
    if i % 5 != 0:
        print('Число не делящееся на пять: ', i)
    else:
        print('Ошибка! Число', i, ' делится на пять!')

