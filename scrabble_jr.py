word = input().split(", ")
word[-1] = word[-1].rstrip()

def getScore(letter):
    if letter in "AE":
        return 1
    if letter in "DR":
        return 2    
    if letter in "BM":
        return 3
    if letter in "VY":
        return 4
    if letter in "JX":
        return 8
    return 0

def getMultiplier(n):
    # returning #lm , wm
    if n%3 == 0 and n%2 == 1:
        return (2,1) 
    if n%5==0:
        return (3,1)
    if n%7 == 0:
        return (1,2)
    if n%8 == 0:
        return (1,3)
    return (1,1)

for _ in range(5):
    pos = int(input())
    finalScore = 0
    wm = 1 # word mult
    for letter in word:
        letterScore = getScore(letter)
        lm, wm0 = getMultiplier(pos)
        wm = max(wm0,wm) # picking the best wm
        finalScore += letterScore * lm
        pos += 1
    print(finalScore * wm)