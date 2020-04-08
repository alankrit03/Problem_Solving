def isprime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    else:
        return True


def give_primes(n):
    i = 0
    num = 2
    while i < 5:
        if isprime(num):
            yield num
            i += 1
        num += 1


prime_list = give_primes(5)
print(*prime_list)

print(__name__)