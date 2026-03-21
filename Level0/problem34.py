# Digit Factorials
import math

def sum_factorial(num):
    total = 0
    for digit in list((int(x) for x in str(num))):
        total += math.factorial(digit)
        
    return total

def solution():
    total = 0
    for n in range(3, 1000000):
        if n == sum_factorial(n):
            total += n
            
    return total

print(solution())