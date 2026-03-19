# Longest Collatz Sequence


def collatz(count, start):
    count += 1
    if start == 1:
        return count
    if start % 2 == 0:
        return collatz(count, start / 2)
    else:
        return collatz(count, 3 * start + 1)
        
        
def find_sequence():
    max= 0
    for i in range(750000, 1000000):
        if collatz(0, i) > max:
            max = collatz(0, i)
            result = i
        
    return result

print(find_sequence())