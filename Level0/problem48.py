# Self Powers

def solution():
    total = 1
    for i in range(2, 1001):
        total += i ** i
        
    return int(str(total)[-10:])

print(solution())