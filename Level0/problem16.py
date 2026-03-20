# Power Digit Sum

def find_sum():
    
    num = 2 ** 1000
    list = []
    for i in range(len(str(num))):
        list.append(int(str(num)[i]))
        
    return sum(list)

print(find_sum())