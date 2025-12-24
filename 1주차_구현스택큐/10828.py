import sys
input = sys.stdin.readline  ## 이거 없으면 오류남 ;;
stack = [] ## 스택 배열 정의 
N = int(input()) ## 명령어 갯수 int 형으로 입력 받기
for i in range(N): ## N 번만큼 반복 그만큼 명령어 받기 위해서
    cmd = input().split() ## 명령어 배열 형식으로 받기 명령어와 push의 숫자값을 받기 위해서

    if cmd[0] == "push":   ## cmd[0] 은 명령어 이름 
        stack.append(int(cmd[1])) ## cmd[1] 은 push의 숫자값 push는 손쉽게 append 사용
    elif cmd[0] == "pop":  ## pop도 손쉽게 pop 사용
        if len(stack) != 0: ## 스택의 길이가 0이 아니라면 = 스택이 비지 않았다면
            print(stack.pop()) ## print를 해줘야지 나옴 그냥 pop하면 사라지기만 함
        else:
            print('-1')
    elif cmd[0] == "size":
        print(len(stack)) ## len으로 스택의 길이 = 요소의 갯수 
    elif cmd[0] == "empty":
        if len(stack) != 0: ## 위와 같이 스택이 비지 않았다면
            print('0')
        else:
            print('1')
    elif cmd[0] == "top":
        if len(stack) != 0:
            print(stack[-1]) ## 배열에서[-1] 은 최상위 요소 반환
        else:
            print('-1')