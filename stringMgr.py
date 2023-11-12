import sys
inputfilename = "res/input_" + __file__.split("\\")[-1][:-3] + ".txt"
sys.stdin = open(inputfilename)
input = sys.stdin.readline

from collections import deque, defaultdict

def getSub(s, e):
    sub = ""
    for i in range(s, e):
        sub += mainString[i]
    return sub

def init(mStr: str):
    global isRev, mainString, di
    isRev = False
    di = defaultdict(int)
    mainString = deque(list(mStr.strip()))
    
    # init hash
    for sl in range(1,5):
        for i in range(len(mainString) - sl + 1):
            sub = getSub(i, i + sl)
            di[sub] += 1

def appendWord(mWord: str):
    mWord = mWord.strip()
    if isRev:
        for ch in mWord:
            mainString.appendleft(ch)
            for sl in range(1,5):
                key = getSub(0,sl)
                di[key] += 1

    else:
        for ch in mWord:
            mainString.append(ch)
            for sl in range(1,5):
                key = getSub(len(mainString) - sl, len(mainString))
                di[key] += 1

def cut(k: int):
    if isRev:
        for ii in range(k):
            for sl in range(1, 5):
                key = getSub(0, sl)
                di[key] -= 1            
            mainString.popleft()
    else:
        for ii in range(k):
            for sl in range(1, 5):
                key = getSub(len(mainString) - sl, len(mainString))
                di[key] -= 1            
            mainString.pop()

def reverse():
    global isRev
    isRev = False if isRev else True

def countOccurrence(mWord: str) -> int:
    if isRev:
        mWord = mWord[::-1]
    return di[mWord]

    

CMD_INIT     = 1
CMD_APPEND   = 2
CMD_CUT      = 3
CMD_REVERSE  = 4
CMD_COUNT    = 5

def run():
    query_cnt = int(input())
    correct = False

    for q in range(query_cnt):
        inputs = iter(input().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            mStr = next(inputs)
            init(mStr)
            correct = True

        elif cmd == CMD_APPEND:
            mWord = next(inputs)
            if correct:
                appendWord(mWord)

        elif cmd == CMD_CUT:
            k = int(next(inputs))
            if correct:
                cut(k)

        elif cmd == CMD_REVERSE:
            if correct:
                reverse()

        elif cmd == CMD_COUNT:
            mWord = next(inputs)
            ret = -1
            if correct:
                ret = countOccurrence(mWord)
            ans = int(next(inputs))
            if ret != ans:
                correct = False
    return correct


def main():
    TC, MARK = map(int, input().split())
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush = True)

if __name__ == '__main__':
    main()
