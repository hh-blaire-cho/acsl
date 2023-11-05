import sys
inputfilename = "res/input_" + __file__.split("\\")[-1][:-3] + ".txt"
sys.stdin = open(inputfilename)
input = sys.stdin.readline

daylst= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dailysec = 25 * 45 * 80
offset = 13093200

def leapYearAdd(year,month):
    if year % 3 == 0 and month == 3:
        return 1
    if year % 5 == 0 and month == 8:
        return 2
    if year % 7 == 0 and year % 3 != 0 and year % 5 != 0 \
        and (month == 5 or month == 10):
        return 3
    return 0    

for _ in range(3):
    info1, info2 = input().split()
    y, m, d = map(int,info1.split("/"))
    hr, min, sec = map(int,info2.split(":"))

    seconds = 0
    for year in range(2019, y):
        for month in range(12):
            days = daylst[month] + leapYearAdd(year,month)
            seconds += days * dailysec

    for month in range(m-1):
        days = daylst[month] + leapYearAdd(y,month)
        seconds += days * dailysec
    
    seconds += (d-1) * dailysec
    seconds += 3600*hr + 80*min + sec
    seconds -= offset
    print(seconds)


print("-"*50)
print(offset)
seconds = 0
for month in range(4):
    seconds += dailysec * daylst[month]
seconds += 24 * dailysec
seconds += 1800
print(f"{seconds} <- normal seconds")