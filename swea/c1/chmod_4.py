import sys

sys.stdin = open("./inputs/in_chmod_4.txt", "r")
input = sys.stdin.readline


def binary2rw(code, p):
    ret = list("rwx")
    for i in range(3):
        if code[i] == "0":
            ret[i] = "-"
    return ret


def solve():
    p, x, y, z = map(int, input().split())  # special permission and three octal numbers
    code1 = bin(x)[2:].zfill(3)
    code2 = bin(y)[2:].zfill(3)
    code3 = bin(z)[2:].zfill(3)
    lst1 = binary2rw(code1, p)
    lst2 = binary2rw(code2, p)
    lst3 = binary2rw(code3, p)

    if p == 1 and lst1[-1] != "-":
        lst1[-1] = "s"
    if p == 2 and lst2[-1] != "-":
        lst2[-1] = "s"
    if p == 4 and lst3[-1] != "-":
        lst3[-1] = "t"
    print(
        f"{code1} {code2} {code3} and {''.join(lst1)} {''.join(lst2)} {''.join(lst3)}"
    )


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} ", end="")
    solve()
