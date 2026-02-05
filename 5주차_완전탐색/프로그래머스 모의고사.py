def solution(answers):
    answer = []
    a,b,c=0,0,0
    ali=[1,2,3,4,5]
    bli=[2, 1, 2, 3, 2, 4, 2, 5]
    cli=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == ali[i%len(ali)]: #if-else문이면, 한명이 맞았을 때 다른 사람들은 체점하지 않음
            a+=1
        if answers[i] == bli[i%len(bli)]:
            b+=1
        if answers[i] == cli[i%len(cli)]:
            c+=1
    max_score=max(a,b,c) #가장 큰 값을 찾은 후
    if max_score==a: # 가장 큰 값과 일치할 경우 리스트에 추가
        answer.append(1)
    if max_score==b:
        answer.append(2)
    if max_score==c:
        answer.append(3)
    return answer