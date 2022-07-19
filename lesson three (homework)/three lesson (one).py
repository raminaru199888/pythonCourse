#
# не код, а печаль... Работает совершенно не так, как задумывалось, запуталась еще в if, код не проходится сначала. Ужасно вообще.
# Но видимо плохо поняла функции с параметрами в какой момент нужно прописывать их, чтобы получилось два условия, ок или не ок..
# можно получить обратную связь по данному заданию.
def reading_data(date1, date2):
    data = input("Введите дату в формате dd.mm.yyyy: ").split('.')
    for i in range(len(data)):
        data[i] = int(data[i])
    list_common = data[::-1]
    # print(list_common) # тест
    if list_common[0] % 4 == 0 and list_common[0] % 100 != 0 or list_common[0] % 400 == 0:
        date1 = 'Високосный год'
    else:
        date2 = 'Не високосный год'
            # print(list_common[0], '- Ошибка! Введены все 0!')
    if list_common[1] == 0 or list_common[1] <= 13:
        date2 = 'Некорретный месяц!'
    else:
        date1 = 'Корретный месяц'
        # print(list_common[1], ' - некорректный месяц!')
    if list_common[2] == 0 or list_common[2] >= 32:
        date2 = 'Некорректное число!'
    else:
        date1 = 'Корректное число!'
        # print(list_common[2], ' - некорректная дата!')
    if list_common[0] == 0 or list_common[1] == 0 or list_common[2] == 0:
        date1 = 'Ошибка! Введены все 0!'
        date2 = 'Ошибка! Введены все 0!'
    else:
        date1 = 'Введены все корректные параметры!'
        date2 = 'Введены все корректные параметры!'
    return date1, date2


date1, date2 = reading_data(0, 0)
print(date1)
print(date2)



# data = input("Введите дату в формате dd.mm.yyyy: ").split('.')
# for i in range(len(data)):
#     data[i] = int(data[i])
# #     list_common.append(data[i])
# list_common = data[::-1]
# print(list_common) # тест
# if list_common[0] % 4 == 0 and list_common[0] % 100 != 0 or list_common[0] % 400 == 0:
#     print(list_common[0], ' - високосный год')  # не поняла как сделать исключение правильно при вводе всех 0
#     try:
#         if list_common[0] == 0 and list_common[1] == 0 and list_common[2] == 0:
#             raise ZeroDivisionError
#     except:
#         print(list_common[0], '- Ошибка! Введены все 0!')
# if list_common[1] == 0 or list_common[1] >= 13:
#     print(list_common[1], ' - некорректный месяц!')
# if list_common[2] == 0 or list_common[2] >= 32:
#     print(list_common[2], ' - некорректная дата!')
