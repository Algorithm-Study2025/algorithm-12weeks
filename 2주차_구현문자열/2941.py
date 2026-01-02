a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] #크로아티아 알파벳 정의 dz= 이 z= 보다 앞에 있어야 함 
s= input().strip() #문자열 저장
for i in a: #크로아티아 앏파벳을 i에 집어넣음
    s = s.replace(i, "*") #크로아티아 알파벳을 *로 변경 한글자 취급
print(len(s))
