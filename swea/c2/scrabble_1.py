import sys

sys.stdin = open("./inputs/in_scrabble_1.txt", "r")
input = sys.stdin.readline


def get_letter_score(c):
    if c in "AE":
        return 1
    elif c in "DR":
        return 2
    elif c in "BM":
        return 3
    elif c in "VY":
        return 4
    elif c in "JX":
        return 8
    return 0


def get_pos_score(x):
    # return (letter_mult, word_mult)
    if x % 3 == 0 and x % 2 != 0:
        return (2, 1)
    if x % 5 == 0:
        return (3, 1)
    if x % 7 == 0:
        return (1, 2)
    if x % 8 == 0:
        return (1, 3)
    return (1, 1)


T = int(input())
for tc in range(1, T + 1):
    lst = input().rstrip().split()
    for subtc in range(1, 6):
        score = 0
        n = int(input())  # starting pos like 12
        word_mult = 1  # will choose the best
        for i in range(len(lst)):
            letter_score = get_letter_score(lst[i])
            (p1, p2) = get_pos_score(n + i)  # letter_mult & word_mult
            word_mult = max(p2, word_mult)
            score += letter_score * p1
        score *= word_mult
        print(f"#{tc}.{subtc} {score}")
