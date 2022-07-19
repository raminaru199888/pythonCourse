from calendar import monthrange

def check_data(number, month, year):
    if year < 0:
        return False
    if month > 12 or month < 0:
        return False
    spesial = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    max_days = monthrange(year, month)[1]
    if number < 1 or number > max_days:
        return False
    return True
data = input("Введите дату в формате dd.mm.yyyy: ").split('.')
# print(data)
number = int(data[0])
month = int(data[1])
year = int(data[2])
if check_data(number, month, year):
    print("OK")
else:
    print("Failed")
