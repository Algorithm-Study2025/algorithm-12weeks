n=int(input())
cnt=0
for _ in range(n):
  string=input()
  if len(string)<=2:
    cnt+=1
    continue
  for i in range(2,len(string)):
    if string[i] in string[:i-1] and string[i]!=string[i-1]:
      break
  else:
    cnt+=1

print(cnt)