import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
M_l = list(map(int, input().split()))
A.sort() ## 이분 탐색을 위해 정렬

for i in M_l: 
    low, high = 0, len(A)-1 ##로우 하이 설정
    find = False ## 찾은 여부 확인 변수
    while low <= high: ## 빠져나온경우는 로우와 하이가 역전되버린 상황 이는 원하는 수를 찾지 못함
        mid = (low+high)//2 ##중간값 설정
        if A[mid] == i: ## A리스트의 중간에 있는 값이 i 원하는 값과 같으면
            find = True ##찾았다!
            break
        elif A[mid] < i: ## A리스트 중간에 있는 값이 i 보다 작으면 로우를 중간 값보다 1 증가
            low = mid+1
        else: ## A리스트 중간에 있는 값이 i 보다 크면 하이를 중간값 -1
            high = mid -1
    if find:
        print(1) ## 찾으면 1
    else:
        print(0) ## 못찾으면 0