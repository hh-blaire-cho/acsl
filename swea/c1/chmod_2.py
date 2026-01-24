import sys

sys.stdin = open("./inputs/in_chmod_2.txt", "r")
input = sys.stdin.readline


def binary2rw(code):
    ret = list("rwx")
    for i in range(3):
        if code[i] == "0":
            ret[i] = "-"
    return "".join(ret)


def bin2dec(x):
    return int(x, 2)


def solve():
    x, y, z = input().split()
    code = str(bin2dec(x)) + str(bin2dec(y)) + str(bin2dec(z))
    print(f"{code} and {binary2rw(x)} {binary2rw(y)} {binary2rw(z)}")


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} ", end="")
    solve()
