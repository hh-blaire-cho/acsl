import sys

sys.stdin = open("./inputs/in_bitstringflicking_3.txt", "r")
input = sys.stdin.readline


def bit_and(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == "1" and b[i] == "1":
            result += "1"
        else:
            result += "0"
    return result


def bit_or(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == "1" or b[i] == "1":
            result += "1"
        else:
            result += "0"
    return result


def bit_xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            result += "1"
        else:
            result += "0"
    return result


def rshift(bits, n):
    length = len(bits)
    if n >= length:
        return "0" * length
    return ("0" * n) + bits[: length - n]


def lshift(bits, n):
    length = len(bits)
    if n >= length:
        return "0" * length
    return bits[n:] + ("0" * n)


def rcirc(bits, n):
    length = len(bits)
    while n >= length:
        n -= length
    return bits[length - n :] + bits[: length - n]


def lcirc(bits, n):
    length = len(bits)
    while n >= length:
        n -= length
    return bits[n:] + bits[:n]


def apply_shift(token):
    op, bits = token.split("-")

    if op.startswith("RSHIFT"):
        n = int(op[6:])
        return rshift(bits, n)
    elif op.startswith("LSHIFT"):
        n = int(op[6:])
        return lshift(bits, n)
    elif op.startswith("RCIRC"):
        n = int(op[5:])
        return rcirc(bits, n)
    elif op.startswith("LCIRC"):
        n = int(op[5:])
        return lcirc(bits, n)


def solve(expression):
    tokens = expression.split()
    result = apply_shift(tokens[0])

    i = 1
    while i < len(tokens):
        operator = tokens[i]
        next_bits = apply_shift(tokens[i + 1])

        if operator == "AND":
            result = bit_and(result, next_bits)
        elif operator == "OR":
            result = bit_or(result, next_bits)
        elif operator == "XOR":
            result = bit_xor(result, next_bits)

        i += 2

    return result


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} {solve(input().strip())}")
