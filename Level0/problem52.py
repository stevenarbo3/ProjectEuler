# Permuted Multiples

def digits(num):
    digits_map = dict()
    for char in list(int(x) for x in str(num)):
        digits_map[char] = digits_map.get(char, 0) + 1
        
    return digits_map

def solution():
    x = 1
    while True:
        if digits(x) == digits(2 * x) and digits(2 * x) == digits(3 * x) and digits(3 * x) == digits(4 * x) and digits(4 * x) == digits(5 * x) and digits(5 * x) == digits(6 * x):
            return x
        x += 1
        
print(solution())
            

