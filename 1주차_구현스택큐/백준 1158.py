import sys
input=sys.stdin.readline

n,k=map(int,input().split())
yo=[n for n in range(1,n+1)]
result=[]
k=k-1
i=0
while len(yo)!=0:
  temp=(i+k)%len(yo)
  result.append(yo[temp])
  yo.remove(yo[temp])
  i=temp
result=str(result).replace("[","<")
result=str(result).replace("]",">")
print(result)