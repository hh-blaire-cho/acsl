import sys

sys.stdin = open("./inputs/in_chmod_2.txt", "r")
input = sys.stdin.readline


def binary2rwx(code):
    ret = list("rwx")
    for i in range(3):
        if code[i] == "0":
            ret[i] = "-"
    return "".join(ret)


def bin2int(x):
    return int(x, 2)


def solve():
    x, y, z = input().split()
    code = str(bin2int(x)) + str(bin2int(y)) + str(bin2int(z))
    print(f"{code} and {binary2rwx(x)} {binary2rwx(y)} {binary2rwx(z)}")


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} ", end="")
    solve()
