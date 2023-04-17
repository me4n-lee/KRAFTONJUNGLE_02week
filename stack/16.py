#https://www.acmicpc.net/problem/2493
#탑
#2493

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

stack = []
result = []
for i in range(n):
    while stack:
        if stack[-1][1] > n_list[i]:
            result.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    else:
        result.append(0)
    stack.append((i, n_list[i]))

print(" ".join(map(str, result)))