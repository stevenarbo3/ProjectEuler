# Number Letter Counts
import math

nums_map = {
    1 : 3,
    2 : 3,
    3 : 5,
    4 : 4,
    5 : 4,
    6 : 3,
    7 : 5,
    8 : 5,
    9 : 4,
    10 : 3,
    11 : 6,
    12 : 6,
    13 : 8,
    14 : 8,
    15 : 7,
    16 : 7,
    17 : 9,
    18 : 8,
    19 : 8,
    20 : 6,
    30 : 6,
    40: 5,
    50 : 5,
    60 : 5,
    70 : 7,
    80 : 6,
    90 : 6,
    100 : 10,
    1000 : 11
}

def letter_counts(limit):
    count = 0
    for i in range(1, limit + 1):

        if math.floor(i / 100) > 0:
            hundreds = int(str(i)[0])
            tens = int(str(i)[1])
            ones = int(str(i)[2])
            
            if tens == 0 and ones == 0:
                count += nums_map[hundreds] + 7
                continue
            if tens == 0:
                count += (nums_map[hundreds]) + 10 + nums_map[ones]
                continue
            if ones == 0:
                count += (nums_map[hundreds]) + 10 + nums_map[tens * 10]
                continue
            
            
            
            count += (nums_map[hundreds]) + 10 + nums_map[tens * 10] + nums_map[ones]
        else:
            tens = int(str(i)[0])
            ones = int(str(i)[1])
            count += nums_map[tens * 10] + nums_map[ones]
            
    return count

print(letter_counts(1000))

        
        