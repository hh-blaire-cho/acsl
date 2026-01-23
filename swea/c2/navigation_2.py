import sys

sys.stdin = open("./inputs/in_navigation_2.txt", "r")
input = sys.stdin.readline

di = {"A": 0, "B": 450, "C": 590, "D": 710, "E": 1030, "F": 1280, "G": 1360}
rtypes = {"I": 65, "H": 60, "M": 55, "S": 45}  # miles per hour
vtypes = {"C": 28, "M": 25, "F": 22, "V": 20}  # miles per gallon

T = int(input())
for tc in range(1, T + 1):
    # starting city, ending city, vehicle type, road type, gas price per gallon
    lst = input().split()

    # calculate distance
    distance = di[lst[1]] - di[lst[0]]

    # calculate time
    time = distance / rtypes[lst[3]]
    hr = str(int(time)).zfill(2)
    mn = str(int(round(60 * (time % 1), 0))).zfill(2)

    # calculate fuel cost
    fuel_cost = distance / vtypes[lst[2]] * float(lst[4])
    print(f"#{tc} {distance} {hr}:{mn} ${fuel_cost:.2f}")
