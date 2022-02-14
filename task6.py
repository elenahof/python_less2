# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []
while input("Добавить товар? Укажите да или нет >>> ") == "да":
    number = int(input("Введите номер товара: "))
    details = {}
    while input("Добавить характеристики товара? Укажите да или нет >>> ") == "да":
        prod_name = input("Введите название товара: ")
        prod_cost = input("Введите стоимость товара: ")
        details[prod_name] = prod_cost
    goods.append(tuple([number, details]))
print(goods)
analysis = {}
for i in goods:
    for prod_name, prod_cost in i[1].items():
        if prod_name in analysis:
            analysis[prod_name].append(prod_cost)
        else:
            analysis[prod_name] = [prod_cost]
print(analysis)