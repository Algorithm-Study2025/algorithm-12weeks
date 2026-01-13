import sys
input = sys.stdin.readline

n = int(input())
xyList =[]
for i in range(n):
    xyList.append(list(map(int,input().split())))
xyList.sort()

for j in xyList:
    print(j[0], j[1])