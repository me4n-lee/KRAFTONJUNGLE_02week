#https://www.acmicpc.net/problem/2504
#괄호의 값
#2504

from collections import deque
import sys
input = sys.stdin.readline

a = list(input().strip())

stack = []
answer = 0
result = 1

for i in range(len(a)):

    if a[i] == "(":
        stack.append(a[i])
        result *= 2

    elif a[i] == "[":
        stack.append(a[i])
        result *= 3

    elif a[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if a[i-1] == "(":
            answer += result
        stack.pop()
        result //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if a[i-1] == "[":
            answer += result

        stack.pop()
        result //= 3

if stack:
    print(0)
else:
    print(answer)