# Sum Square DIfference

def sum_square_difference(limit):
    sum_of_square = 0
    square_of_sum = 0
    for i in range(1, limit + 1):
        sum_of_square += i**2
        square_of_sum += i
        
    square_of_sum = square_of_sum**2
    
    return square_of_sum - sum_of_square

print(sum_square_difference(100))