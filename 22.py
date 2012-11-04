names = open(r"C:\users\no309c\Desktop\names.txt").read()
names = names.replace('"', '').split(',')
names.sort()

def get_score(char):
    return ord(char) - ord('A') + 1
    
scores = []
for name in names:
    score = 0
    for char in name:
        score += get_score(char)
    scores.append(score)
    
    
    
print sum(score*(i+1) for i,score in enumerate(scores))