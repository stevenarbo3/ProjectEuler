
def sum_odd_squares(limit):
    sum = 0
    for x in range(limit + 1):
        square = x * x
        if square % 2 == 1:
            sum += square
            
    return sum

print(sum_odd_squares(226000))