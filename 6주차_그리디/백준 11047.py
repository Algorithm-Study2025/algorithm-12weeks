import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coin=[]
result=0

for _ in range(n):
  coin.append(int(input().strip()))

coin.sort(reverse=True)

for c in coin:
  if k>=c:
    result+=k//c #while문이 아니라, 몫과 나머지를 구하면 더 빠른 거였음
    k%=c
print(result)