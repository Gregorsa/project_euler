'''10001-ое простое число
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?'''

lst_primes = [2, 3]
current = 4

while len(lst_primes) < 10001:
    for n in lst_primes:
        if current % n == 0:
            break
    else:
        lst_primes.append(current)
    current += 1

print(lst_primes[-1])