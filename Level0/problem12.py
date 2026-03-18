# Highly Divisible Triangular Numbers

def find_divisors(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            
    return count * 2
        

def find_triangle_num():
    tri, i = 1, 1
    divisors = 1
    while divisors < 500:
        i += 1
        tri += i
        divisors = find_divisors(tri)
        if divisors > 200:
            print(divisors)
        
    return tri

print(find_triangle_num())

print(find_divisors(28))
