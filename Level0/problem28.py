# Number Spiral Diagonals
# Found pattern in spiral  to create algorithm

def solution():
    corner = 1
    factor = 2
    total = 1
    while corner < (1001 ** 2):
        for i in range(1, 5):
            corner += factor
            total += corner
        factor += 2
        
    return total
        
print(solution())