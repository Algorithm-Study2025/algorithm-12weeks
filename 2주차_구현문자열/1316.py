n = int(input()) #문자열 갯수
result = n #문자열 개수를 결과에 저장
for _ in range(n): # 문자열 개수 만큼 반복
    slist = input() # 그룹단어를 저장
    for i in range(len(slist)-1): #그룹단어의 길이 만큼 반복
        if slist[i] == slist[i+1]: #현재 글자와 그 뒤 글자가 같으면 건너뜀
            continue
        elif slist[i] in slist[i+1 :]: #현재 글자가 다음글자 이후에 글자가 존재하면 그룹단어가 아니므로 1을 뺌
            result -= 1
            break
print(result)