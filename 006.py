'''Разность между суммой квадратов и квадратом суммы

Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.'''

import time

start_time = time.time()
numList = []
for x in range(1, 101):
    numList.append(x)
    x += 1
sum1 = sum(i * i for i in numList)
sum2 = (sum(i for i in numList)) ** 2
print(sum2 - sum1)

print("%s секунд" % (time.time() - start_time))
