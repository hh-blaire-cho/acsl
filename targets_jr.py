rMoveDict={"A":0,"B":-1,"C":0,"D":1,"E":-1,"F":-1,"G":1,"H":1}
cMoveDict={"A":-1,"B":0,"C":1,"D":0,"E":-1,"F":1,"G":1,"H":-1}

def search(row0,col0):
    global maxcount, answer
    for dir in "ABCDEFGH":
        row, col = row0, col0
        cnt = 0
        while True:
            row += rMoveDict[dir]
            col += cMoveDict[dir]
            if row >= n or col >= n or row < 0 or col < 0:
                break
            if f"{row}{col}" not in targets:
                break
            cnt += 1
        if cnt > maxcount:
            answer = f"{row0}{col0}{dir}"
            maxcount = cnt

for _ in range(5):
    n = int(input())
    targets = set(input().split())
    maxcount = 0
    answer = "00A"

    #top horiz
    for i in range(n-1):
        row, col = 0, i
        search(row, col)

    #right vert
    for i in range(n-1):
        row, col = i, n-1
        search(row, col)

    #bot horiz
    for i in range(n-1):
        row, col = n-1,i+1
        search(row, col)

    #left vert
    for i in range(n-1):
        row, col = i+1, 0
        search(row, col)

    print(answer)
