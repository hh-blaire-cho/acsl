inputfilename = "res/input_" + __file__.split("\\")[-1][:-3] + ".txt"
import sys
sys.stdin = open(inputfilename)
input = sys.stdin.readline

def conv(n):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
            'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}[n]

def updateFrequency(lst,base):
    for k in range(base):
        k_cnt = lst.count(k)
        freqList[k] += k_cnt


def findModeCount(ntimes, base, start):
    lst = list(start)
    lst = list(map(conv, lst))
    updateFrequency(lst,base)
    for _ in range(ntimes - 1):
        carry = 0
        lst[-1] += 1
        for j in range(len(lst)-1,-1,-1):
            lst[j] += carry
            if lst[j] < base:
                carry = 0
                break
            carry = 1
            lst[j] = 0
        if lst[0] == 0:
            lst = [1] + lst
        updateFrequency(lst,base)
    return max(freqList)    


for _ in range(5):
    n, b, s = input().split()
    n, b = map(int,(n,b))
    freqList = [0]*b
    print(findModeCount(n,b,s))
