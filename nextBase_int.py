def countLargestDigit(ntimes, base, start):
    lst = list(map(int, list(str(start))))
    ans = lst.count(base-1)
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
        ans += lst.count(base-1)
    return ans

for _ in range(5):
    n, b, s = map(int, input().split())
    print(countLargestDigit(n,b,s))