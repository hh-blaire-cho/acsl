def searchFoward(sub, string):
    where = string.find(sub)
    if where == -1:
        return (False, string)
    string = string[:where] + string[where+len(sub):]
    return (True, string)


def searchBackward(sub, string):
    if string.find(sub) == -1:
        return (False, string)
    for i in range(len(string) - len(sub), -1, -1):
        sliced = string[i:i+len(sub)]
        if sliced == sub:
            string = string[:i] + string[i + len(sub):]
            return (True, string)
    return (False, string)


def bin2oct(s):
    if len(s) % 3 == 1:
        s = "00" + s
    elif len(s) % 3 == 2:
        s = "0" + s

    ret = ""
    for i in range(0, len(s), 3):
        tot = 0
        sliced = s[i:i+3]
        if sliced[0] == "1":
            tot += 4
        if sliced[1] == "1":
            tot += 2
        if sliced[2] == "1":
            tot += 1
        ret += str(tot)
    return str(int(ret))


for _ in range(5):
    binString = ""
    for letter in input().rstrip():
        binString += bin(ord(letter))[2:].zfill(8)

    num = -1
    while True:
        num += 1
        sub = bin(num)[2:]
        b1, binString = searchFoward(sub, binString)
        b2, binString = searchBackward(sub, binString)
        if not any((b1, b2)):
            break

    octString = bin2oct(binString)

    num = -1
    while True:
        num += 1
        sub = oct(num)[2:]
        b1, octString = searchFoward(sub, octString)
        b2, octString = searchBackward(sub, octString)
        if not any((b1, b2)):
            break
    print(num-1)
