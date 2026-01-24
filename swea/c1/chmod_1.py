import sys

sys.stdin = open("./inputs/in_chmod_1.txt", "r")
input = sys.stdin.readline


def binary2rwx(code):
    ret = list("rwx")
    for i in range(3):
        if code[i] == "0":
            ret[i] = "-"
    return ret


def solve():
    x, y, z = map(int, input().split())
    code1 = bin(x)[2:].zfill(3)
    code2 = bin(y)[2:].zfill(3)
    code3 = bin(z)[2:].zfill(3)
    lst1 = binary2rwx(code1)
    lst2 = binary2rwx(code2)
    lst3 = binary2rwx(code3)
    print(
        f"{code1} {code2} {code3} and {''.join(lst1)} {''.join(lst2)} {''.join(lst3)}"
    )


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} ", end="")
    solve()
