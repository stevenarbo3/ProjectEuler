def fibonacci(limit):
    prev, curr = 1, 1
    sum = 0
    while curr < limit:
        
        if curr % 2 == 0:
            sum += curr
        
        next = prev + curr
        prev = curr
        curr = next
        
    return sum

print(fibonacci(4000000))
        
        
        