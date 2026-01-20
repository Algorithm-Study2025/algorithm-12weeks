import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

# 딕셔너리로 숫자의 등장 횟수 기록
count_dict = {}

for num in N_list:
    if num in count_dict: 
        count_dict[num] += 1 ## 숫자가 이미 딕셔너리에 존재하면 +1
    else:
        count_dict[num] = 1 ## 숫자가 존재 하지 않으면 1로 저장

# M_list의 숫자가 N_list에 몇 번 등장했는지 출력
for num in M_list:
    if num in count_dict:
        print(count_dict[num], end=" ")
    else:
        print(0, end=" ")