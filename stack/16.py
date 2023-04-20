#https://www.acmicpc.net/problem/2493
#탑
#2493

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

stack = []
result = []
#스택에는 (인덱스, 높이) 형태의 튜플을 저장
for i in range(n):
    while stack:
        if stack[-1][1] > n_list[i]:
            # +1을 해주는 이유는 탑의 순서가 0부터가 아닌 1부터 이기 때문!
            result.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    else:
        result.append(0)
    stack.append((i, n_list[i]))

print(" ".join(map(str, result)))