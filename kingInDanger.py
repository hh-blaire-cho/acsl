import sys
inputfilename = "res/input_" + __file__.split("\\")[-1][:-3] + ".txt"
sys.stdin = open(inputfilename)
input = sys.stdin.readline

di = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

def pawn(row0,col0):
    return [(row0-1, col0+1), (row0-1, col0-1)]

def knight(row0,col0):
    return [(row0-2, col0-1), (row0-2, col0+1), (row0+2, col0-1),(row0+2, col0+1),\
            (row0+1, col0-2), (row0+1, col0+2), (row0-1, col0-2), (row0-1, col0+2)]

def rook(r0,c0):
    rkSpaces = list()

    for r1 in range(r0+1, 8):
        if board[r1][c0] != " " or r1>=8:
            break
        rkSpaces.append((r1,c0))

    for r1 in range(r0-1, -1, -1):
        if board[r1][c0] != " " or r1<0:
            break
        rkSpaces.append((r1,c0))

    for c1 in range(c0+1, 8):
        rkSpaces.append((r0, c1))
        if board[r0][c1] != " " or c1>=8:
            break

    for c1 in range(c0-1, -1, -1):
        if board[r0][c1] != " " or c1<0:
            break
        rkSpaces.append((r0, c1))

    return rkSpaces

def bishop(r0,c0):
    biSpaces=list()

    r1, c1 = r0, c0
    while True:
        r1+=1
        c1+=1
        if r1<0 or c1<0 or r1>=8 or c1>=8 or board[r1][c1] != " ":
            break
        biSpaces.append((r1,c1))

    r1, c1 = r0, c0
    while True:
        r1-=1
        c1+=1
        if r1<0 or c1<0 or r1>=8 or c1>=8 or board[r1][c1] != " ":
            break
        biSpaces.append((r1,c1))

    r1, c1 = r0, c0
    while True:
        r1+=1
        c1-=1
        if r1<0 or c1<0 or r1>=8 or c1>=8 or board[r1][c1] != " ":
            break
        biSpaces.append((r1,c1))

    r1, c1 = r0, c0
    while True:
        r1-=1
        c1-=1
        if r1<0 or c1<0 or r1>=8 or c1>=8 or board[r1][c1] != " ":
            break
        biSpaces.append((r1,c1))

    return biSpaces

def findBadSpaces(otherPos):
    for t, r, c in otherPos:
        r, c = map(int, (r,c))
        if t == "P":
            for newBad in pawn(r,c):
                badSpaces.add(newBad)
        if t == "N":
            for newBad in knight(r,c):
                badSpaces.add(newBad)
        if t == "R":
            for newBad in rook(r,c):
                badSpaces.add(newBad)
        if t == "B":
            for newBad in bishop(r,c):
                badSpaces.add(newBad)
        if t == "Q":
            for newBad in rook(r,c):
                badSpaces.add(newBad)
            for newBad in bishop(r,c):
                badSpaces.add(newBad)

def findKingSpaces(kingPos):
    for rm in [-1,0,1]:
        for cm in [-1,0,1]:
            if rm == 0 and cm == 0:
                continue
            r1 = kingPos[0] + rm
            c1 = kingPos[1] + cm
            if r1<0 or c1<0 or r1>=8 or c1>=8:
                continue   
            if (r1,c1) in badSpaces:
                continue         
            kingSpaces.add((r1,c1))

def find_king_status(info):
    otherPos = list()
    for piece in info.rstrip().split(" "):
        typ, pos1, pos2 = piece[0], piece[1], piece[2]
        r = 7-(int(pos2)-1)
        c = di[pos1]
        if typ == "K":
            kingPos = (r,c)
        else:
            board[r][c] = typ
            otherPos.append(f"{typ}{r}{c}")
    
    findBadSpaces(otherPos)
    findKingSpaces(kingPos)

    if kingPos in badSpaces:
        if len(kingSpaces)==0:
            return "CHECKMATE" 
        return "CHECK"
    else:
        if len(kingSpaces)==0:
            return "STALEMATE"
        return "SAFE"



for _ in range(5):
    badSpaces = set()
    kingSpaces = set()
    board = [[" " for c in range(8)] for r in range(8)]
    pieces = input()
    print(find_king_status(pieces))