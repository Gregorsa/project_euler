'''Наименьшее кратное
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?'''

import time

start_time = time.time()


def nod(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def nok(a, b):
    return a * b // nod(a, b)


d = 1  # В нем будет хранится значение предыдущего НОК
for i in range(2, 21):  # Перебераем делители
    d = nok(d, i)  # Ищем их НОК
print(d)
print("%s секунд" % (time.time() - start_time))
