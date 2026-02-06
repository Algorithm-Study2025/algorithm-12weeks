import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cardList = list(map(int, input().split()))
bestSum = 0
# for문을 3개 써서 for문을 도는동안 모든 조합을 찾으면서 고르는 카드들이 곂치지 않게 뽑음
for i in range(N-2): # 0 부터 n-3
    for j in range(i+1, N-1): # i+1 부터 n-2 
        for k in range(j+1, N): # j+1 부터 n-1
            currentSum = cardList[i] + cardList[j] + cardList[k] 
            if currentSum == M: # 찾으면 종료
                print(currentSum)
                exit()
            elif currentSum <= M: 
                if currentSum > bestSum: #bestSum 보다 더 M에 가까운 값을 찾으면 그값 저장
                    bestSum = currentSum

print(bestSum)


