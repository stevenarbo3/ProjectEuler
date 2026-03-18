# 10001st Prime

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime(limit):
    x = 1
    count = 0
    while count != limit:
        x += 1
        if is_prime(x):
            count += 1
            
            
    return x
print(find_prime(10001))
            