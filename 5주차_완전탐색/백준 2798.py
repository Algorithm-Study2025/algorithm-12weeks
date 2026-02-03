import sys
input=sys.stdin.readline

n,m=map(int,input().split())
card=list(map(int,input().split()))

result=0

for i in range(n-2): #O(100)
  for j in range(i+1,n): #O(100)
    for k in range(j+1,n): #O(100)
      temp=card[i]+card[j]+card[k]
      if temp<=m:
        result=max(result,temp)
print(result)

#O(1000000)