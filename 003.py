'''Наибольший простой делитель
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?'''

import math
import time

start_time = time.time()


def issimple(x):
    y = math.ceil(math.sqrt(x))
    lst = []
    for i in range(3, y):
        if x % i == 0:
            if issimple(i) == []:
                lst.append(i)
    return lst


x = issimple(600851475143)
print(max(x))
print("%s секунд" % (time.time() - start_time))
