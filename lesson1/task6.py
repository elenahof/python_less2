# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = float(input("Введите результат первого дня >>> "))
b = float(input("Введите необходимый результат >>> "))
day_count = 1
if a > b:
    print(day_count)
while a < b:
    a = a + a/10
    day_count = day_count + 1
    print(day_count)