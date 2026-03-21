# Coded Triangle Numbers

def solution():
    tri = {}
    for n in range(100):
        tri[0.5 * n * (n + 1)] = n
    
    with open('assets/words.txt', 'r') as file:
        words = file.read().split(',')
        count = 0
        for word in words:
            word = word.replace('"', '')
            value = sum(list(ord(x) - 64 for x in word))
            if value in tri:
                count += 1
                
    file.close()
    return count

print(solution())