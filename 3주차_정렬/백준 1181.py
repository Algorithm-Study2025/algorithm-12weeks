import sys
input=sys.stdin.readline

result=[]
n=int(input())
for _ in range(n):
  result.append(input().strip())

#중복제거
result=list(set(result))

#길이 짧은것, 사전 순
result.sort(key=lambda x : (len(x),x))

for r in result:
  print(r)