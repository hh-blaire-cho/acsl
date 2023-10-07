for _ in range(5):
    binString = ""
    for letter in input().rstrip():
        binString += bin(ord(letter))[2:].zfill(8)
    num = -1
    while True:
        num += 1
        sub = bin(num)[2:]
        if binString.find(sub) == -1:
            break
    print(num - 1)