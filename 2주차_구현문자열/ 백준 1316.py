n=int(input())
cnt=0
for _ in range(n):
  string=input()
  if len(string)<=2:
    cnt+=1
    continue
  for i in range(2,len(string)):
    if string[i] in string[:i-1] and string[i]!=string[i-1]: #단순히 현재 문자와 -2위치부터 처음까지의 문자 집합이 같으면 그룹 문자가 아닐 줄 알았는데, 3개가 나란한 경우를 고려하지 않음
      break
  else:
    cnt+=1

print(cnt)