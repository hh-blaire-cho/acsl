import sys

sys.stdin = open("./inputs/in_navigation_1.txt", "r")
input = sys.stdin.readline

di = {"A": 0, "B": 450, "C": 590, "D": 710, "E": 1030, "F": 1280, "G": 1360}

T = int(input())
for tc in range(1, T + 1):
    miles, cost, vel = map(float, input().split())  # velocity = mph
    for subtc in range(1, 6):
        p, q = input().split()
        distance = di[q] - di[p]
        time = distance / vel
        hr = str(int(time)).zfill(2)
        mn = str(int(round(60 * (time % 1), 0))).zfill(2)
        fuel_cost = distance * cost / miles
        print(f"#{tc}-{subtc}, {hr}:{mn}, ${fuel_cost:.2f}")
