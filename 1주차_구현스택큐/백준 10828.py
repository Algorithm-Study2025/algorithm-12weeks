# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input=sys.stdin.readline # 이 부분 없으면 시간 초과 남

stack=[]
def push(X):
  stack.append(X)
def pop():
  if len(stack)==0:
    print(-1)
  else:
    print(stack.pop())
def size():
  print(len(stack))
def empty():
  if len(stack)==0:
    print(1)
  else:
    print(0)
def top():
  if len(stack)==0:
    print(-1)
  else:
    print(stack[-1])

n=int(input())
for _ in range(n):
  a=list(input().split())
  if a[0]=='push':
    push(a[1])
  elif a[0]=='pop':
    pop()
  elif a[0]=='size':
    size()
  elif a[0]=='empty':
    empty()
  elif a[0]=='top':
    top()