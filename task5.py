# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

number = int(input("Введите новый элемент рейтинга >>> "))
rating = [7, 5, 3, 3, 2]
i = rating.count(number)
for x in rating:
    if i > 0:
        a = rating.index(number)
        rating.insert(i + a, number)
        break
    else:
        if number > x:
            b = rating.index(x)
            rating.insert(b, number)
            break
        elif number < rating[len(rating) - 1]:
            rating.append(number)
print(rating)