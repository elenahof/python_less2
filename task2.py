# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

new_list = input("Введите элементы списка без пробелов >>> ")
change_list = list(new_list)
print(f'Изначальный список: {change_list}')
if len(change_list) % 2 == 0:
    i = 0
    while i < len(change_list):
        x = change_list[i]
        change_list[i] = change_list[i + 1]
        change_list[i + 1] = x
        i = i + 2
else:
    i = 0
    while i < len(change_list) - 1:
        x = change_list[i]
        change_list[i] = change_list[i + 1]
        change_list[i + 1] = x
        i = i + 2
print(f'Новый список: {change_list}')

