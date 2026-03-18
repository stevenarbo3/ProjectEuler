# Largest Palindrome Product
# between two, three digit numbers thus the limit is 999 * 999 = 998001 and min is 100 * 100 = 10000

def is_palindrome(num):
    x, y = 0, len(num) - 1
    while x < len(num) / 2:
        if num[x] != num[y]:
            return False
        x += 1
        y -= 1
        
    return True
            
    return True

def largest_palindrome_product(limit):
    result = 0
    for i in range(limit, 99, -1):
        for j in range(limit, 99, -1):
            product = i * j
            if is_palindrome(str(product)):
                result = max(result, product)
                
        
    return result

print(largest_palindrome_product(999))
        