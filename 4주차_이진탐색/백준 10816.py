import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
a.sort()

m=int(input())
b=list(map(int,input().split()))

result=[]

def lower_bound(key):
  left,right=0,n
  while left<right:
    mid=(left+right)//2
    if a[mid]<key: #key를 만나도 왼쪽으로 당김
      left=mid+1
    else:
      right=mid
  return left

def upper_bound(key):
  left,right=0,n
  while left<right:
    mid=(left+right)//2
    if a[mid]<=key: #key를 만나면 오른쪽으로 당김
      left=mid+1
    else:
      right=mid
  return left

for i in b:
  temp=upper_bound(i)-lower_bound(i)
  result.append(temp)
print(*result)