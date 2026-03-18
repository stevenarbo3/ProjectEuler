def sum_natural_numbers(limit):
    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        
    return sum

print(sum_natural_numbers(1000))