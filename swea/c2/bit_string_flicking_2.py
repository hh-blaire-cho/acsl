import sys

sys.stdin = open("./inputs/in_bitstringflicking_2.txt", "r")
input = sys.stdin.readline


def bit_and(x, y):
    ret = ""
    for i in range(len(x)):
        if x[i] == "1" and y[i] == "1":
            ret += "1"
        else:
            ret += "0"
    return ret


def bit_or(x, y):
    ret = ""
    for i in range(len(x)):
        if x[i] == "1" or y[i] == "1":
            ret += "1"
        else:
            ret += "0"
    return ret


def bit_xor(x, y):
    ret = ""
    for i in range(len(x)):
        if x[i] != y[i]:
            ret += "1"
        else:
            ret += "0"
    return ret


def solve(s):
    tokens = s.split()
    result = tokens[0]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        nxt = tokens[i + 1]
        if op == "AND":
            result = bit_and(result, nxt)
        elif op == "OR":
            result = bit_or(result, nxt)
        else:
            result = bit_xor(result, nxt)
        i = i + 2
    return result


T = int(input())
for tc in range(1, T + 1):
    s = input()
    print(f"#{tc} {solve(s)}")
