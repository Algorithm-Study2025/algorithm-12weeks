import sys
input=sys.stdin.readline

result=[]
n=int(input())
for _ in range(n):
  x,y=map(int,input().split())
  result.append([x,y])
result.sort() #2차원 리스트일 경우, 0열 비교 - 같으면, 1열 비교
for r in result:
  print(r[0],r[1])