#https://www.acmicpc.net/problem/10000
#원 영역
#10000

import sys
input = sys.stdin.readline

n = int(input())
n_list = []
events = []
for i in range(n):
    x, r = map(int, input().split())
    n_list.append([x, r])

    left = x - r
    right = x + r

    events.append((left, '('))  # 원의 왼쪽 경계에 '('를 할당하여 시작 이벤트를 나타낸다.
    events.append((right, ')'))  # 원의 오른쪽 경계에 ')'를 할당하여 종료 이벤트를 나타낸다.

events.sort()

cnt = 1
stack = []
for _, event in events:
    if event == '(':  # 시작 이벤트인 경우
        if not stack:  # 스택이 비어 있으면 새로운 영역이 시작되므로 영역 개수를 증가시킨다.
            cnt += 1
        elif len(stack) >= 2:  # 스택의 길이가 2 이상이면 3원이 완벽하게 내접하는 경우로 간주하고 cnt를 추가로 증가시킨다.
            cnt += 1
        stack.append(event)
    else:  # 종료 이벤트인 경우
        stack.pop()
        if not stack:  # 스택이 비어 있으면 영역이 종료되므로 영역 개수를 증가시킨다.
            cnt += 1

print(cnt)