import sys

sys.stdin = open("./inputs/in_chmod_3.txt", "r")
input = sys.stdin.readline


def rw2binary(code):
    ret = list("111")
    for i in range(3):
        if code[i] == "-":
            ret[i] = "0"
    return "".join(ret)


def bin2dec(x):
    return int(x, 2)


def solve():
    x, y, z = map(rw2binary, input().split())
    octal = str(bin2dec(x)) + str(bin2dec(y)) + str(bin2dec(z))
    print(f"{octal} and {x} {y} {z}")


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} ", end="")
    solve()
