# Amicable Numbers

def divisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
            
    return total

def solution():
    proper_divisors_map = dict()
    total = 0
    for i in range(2, 10000):
        sum_divisors = divisors(i)
        if sum_divisors in proper_divisors_map and proper_divisors_map[sum_divisors] == i:
            total += sum_divisors + i
            continue
            
        proper_divisors_map[i] = sum_divisors
        
    return total

print(solution())
    
    
            
        