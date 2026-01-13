import sys
input = sys.stdin.readline

n = int(input())
numList = []
for i in range(n):
    numList.append(int(input()))

numList.sort()
for j in numList:
    print(j)