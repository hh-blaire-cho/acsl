import sys

sys.stdin = open("./inputs/in_scrabble_3.txt", "r")
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
    # return (letter_mult, word_ult)
    if x in range(3, 40, 6):
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
    word = input().rstrip().split()
    for subtc in range(1, 6):
        scores = []
        lst = input().split()
        for i in range(0, len(lst), 2):
            pos = int(lst[i])
            dir = lst[i + 1]
            score = 0
            word_mult = 1  # will choose the best
            move = 10 if dir == "V" else 1
            for c in word:
                letter_score = get_letter_score(c)
                (p, q) = get_pos_score(pos)
                word_mult *= q
                score += letter_score * p
                pos = pos + move
            score = score * word_mult
            scores.append(score)

        print(f"#{tc}.{subtc} {max(scores)}")
