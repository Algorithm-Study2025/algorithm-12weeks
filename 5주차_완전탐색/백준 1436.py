import sys
input=sys.stdin.readline

n=int(input())
cnt=0
start=665 # 666으로 시작하기 위함
while cnt<n: #카운트 값이 n에 도달하는 순간 종료, O(n)
  start+=1
  if "666" in str(start): #O(log n)
    cnt+=1
print(start)

#O(n log n)