# Largest Prime Number
# Had to speed it up - reduced range to only check numbers to and from the square root of the limit
# Also reversed the search order and returned the first valid number found, aka the max

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(limit):
    for i in range(int(limit ** 0.5), 2, -1):
        if limit % i == 0 and is_prime(i):
            return i
            
    return "Did not compute"

print(largest_prime_factor(600851475143))
