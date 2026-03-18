# Smallest Mulitple

def smallest_multiple(nums):
    result = 2520
    while True:
        for i in range(1, nums + 1):
            if result % i != 0:
                break
            if i == nums:
                return result
        result += 1
        
    return "Did not compute"

print(smallest_multiple(20))