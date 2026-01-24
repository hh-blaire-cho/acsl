import sys

sys.stdin = open("./inputs/in_chmod_3.txt", "r")
input = sys.stdin.readline


def rwx2binary(code):
    ret = list("111")
    for i in range(3):
        if code[i] == "-":
            ret[i] = "0"
    return "".join(ret)


def bin2int(x):
    return str(int(x, 2))


def solve():
    x, y, z = map(rwx2binary, input().split())
    octal = bin2int(x) + bin2int(y) + bin2int(z)
    print(f"{octal} {x} {y} {z}")


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} ", end="")
    solve()
