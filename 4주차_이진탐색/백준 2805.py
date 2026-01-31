import sys
input=sys.stdin.readline

n,m=map(int,input().split())
log=list(map(int,input().split()))

answer=0
low,high=0,max(log)
while low<=high:
  mid=(low+high)//2
  temp=0
  for l in log:
    if (l-mid)>0: #음수가 나올경우는 필요 없음
      temp+=l-mid 
  if temp<m: #잘라가는 통나무가 적을때, 높이가 더 낮아야 함
    high=mid-1
  elif temp>=m: #잘라가는 통나무가 많을 때, 높이가 더 높아야 함
    low=mid+1
    answer=mid #조건 만족할 때의 값 저장
print(answer)