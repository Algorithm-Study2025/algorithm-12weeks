import re
new_id = input()
new_id = new_id.lower() # 소문자화
new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id) #허용되지 않는 문자 제거
new_id = re.sub(r'\.{2,}', '.', new_id) #반복되는 마침표 제거
new_id = new_id.strip('.') #양끝 마침표 제거
if len(new_id) == 0: #빈문자열이면 a 삽입
    new_id = 'a'
if len(new_id) >= 16: #16자 이상이면 15자만 남기기
    new_id = new_id[:15]
new_id = new_id.rstrip('.') #오른쪽 끝 마침표 제거
if len(new_id) <= 2: #2자 이하 마지막 글자 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
print(new_id)

