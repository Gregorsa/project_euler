'''Наибольшее произведение-палиндром
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.'''

import time

start_time = time.time()
palindrom = []
for i in range(100, 1000):
    for j in range(100, 1000):
        number = str(i*j)
        if (number == number[::-1]):
            palindrom.append(int(number))
print(max(palindrom))
print("%s секунд" % (time.time() - start_time))