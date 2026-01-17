import sys
input=sys.stdin.readline

n=int(input())
first=list(map(int,input().split())) #이진 탐색의 정렬을 안 함
first.sort()

def binary_search(arr,key):
  left=0
  right=len(arr)-1
  while left<=right: ##
    mid=(left+right)//2
    if arr[mid]==key:
      return 1
    elif arr[mid]<key:
      left=mid+1
    else:
      right=mid-1
  return 0

m=int(input())
sec=list(map(int,input().split()))

for s in sec:
  print(binary_search(first,s))