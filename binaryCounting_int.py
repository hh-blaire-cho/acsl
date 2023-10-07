def searchFoward(sub):
    global binString
    where = binString.find(sub)
    if where == -1:
        return False
    binString = binString[:where] + binString[where+len(sub):]
    return True

def searchBackward(sub):
    global binString
    if binString.find(sub) == -1:
        return False
    for i in range(len(binString) - len(sub),-1,-1):
        sliced = binString[i:i+len(sub)]
        if sliced == sub:
            binString = binString[:i] + binString[i + len(sub):]
            return True
    return False


for _ in range(5):
    binString = ""
    for letter in input().rstrip():
        binString += bin(ord(letter))[2:].zfill(8)

    num = -1
    while True:
        num += 1
        sub = bin(num)[2:]
        if not any((searchFoward(sub), searchBackward(sub))):
            break
    print(num-1)