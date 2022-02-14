# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через list
month_number = int(input("Введите номер месяца >>> "))
month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
              'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
if (month_number <= 12 and month_number >= 1):
    if month_number == 1 or month_number == 2 or month_number == 12:
        print(f'{month_list[month_number - 1]} это {season_list[0]}')
    if month_number == 3 or month_number == 4 or month_number == 5:
        print(f'{month_list[month_number - 1]} это {season_list[1]}')
    if month_number == 6 or month_number == 7 or month_number == 8:
        print(f'{month_list[month_number - 1]} это {season_list[2]}')
    if month_number == 9 or month_number == 10 or month_number == 11:
        print(f'{month_list[month_number - 1]} это {season_list[3]}')
else:
    print("Введено некорректное число. Введите число от 1 до 12!")


# Решение через dict
month_num = int(input("Введите номер месяца >>> "))
season_dict = {"wint": 'Зима', "spr": 'Весна', "summ": 'Лето', "aut": 'Осень'}
if (month_num <= 12 and month_num >= 1):
    if month_num == 1 or month_num == 2 or month_num == 12:
        print(season_dict.get("wint"))
    if month_num == 3 or month_num == 4 or month_num == 5:
        print(season_dict.get("spr"))
    if month_num == 6 or month_num == 7 or month_num == 8:
        print(season_dict.get("summ"))
    if month_num == 9 or month_num == 10 or month_num == 11:
        print(season_dict.get("aut"))
else:
    print("Введено некорректное число. Введите число от 1 до 12!")