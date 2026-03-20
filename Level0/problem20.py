# Factorial Digit Sum

def solution(num):
    curr = 1
    for i in range(2, num + 1):
        curr *= i
        
    chars = list(int(x) for x in str(curr))
    return sum(chars)

print(solution(100))