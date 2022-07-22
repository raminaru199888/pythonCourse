# Китайский гороскоп делит время на 12-летние циклы, и каждому году соответствует конкретное животное.
# После окончания одного цикла начинается другой, то есть 2012 год снова символизирует дракона
# Программа принимает на вход одно число - год.


year = [int(i) for i in input('Введите год:').split()]
if 2000 in year:
    print("Дракон")
elif 2001 in year:
    print("Змея")
elif 2002 in year:
    print("Лошадь")
elif 2003 in year:
    print("Коза")
elif 2004 in year:
    print("Обезьяна")
elif 2005 in year:
    print("Петух")
elif 2006 in year:
    print("Собака")
elif 2007 in year:
    print("Свинья")
elif 2008 in year:
    print("Крыса")
elif 2009 in year:
    print("Бык")
elif 2010 in year:
    print("Тигр")
elif 2011 in year:
    print("Кролик")
else:
    print("Некорректный год!")


