# 1000 digit fibonacci

def solution():
    count = 2
    prev, curr = 1, 1
    while len(str(curr)) < 1000:
        next = prev + curr
        prev = curr
        curr = next
        count += 1
    return count

print(solution())