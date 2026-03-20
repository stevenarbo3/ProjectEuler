# Names Scores



def solution():
    
    with open('assets/names.txt', 'r') as file:
        names = file.read().split(',')
        names.sort()
        score = 0
        count = 1
        for name in names:
            name = name.replace('"', '')
            value = sum(list(ord(x) - 64 for x in name))
            score += value * count
            count += 1
            
        return score
            
            
        
print(solution())