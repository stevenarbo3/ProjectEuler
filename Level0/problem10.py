# Summation of Primes

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes(limit):
    sum = 0
    for i in range(2, limit):
        if is_prime(i):
            sum += i
            
    return sum

print(sum_primes(2000000))