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

    events.append((left, -1))  # 원의 왼쪽 경계에 -1를 할당하여 시작 이벤트를 나타낸다.
    events.append((right, 1))  # 원의 오른쪽 경계에 1를 할당하여 종료 이벤트를 나타낸다.

events.sort()

cnt = 1
stack = []
for _, event in events:
    if event == -1:  # 시작 이벤트인 경우
        stack.append(event)
        if len(stack) > 1:  # 스택의 길이가 2 이상이면 내접하는 원이 있는 것으로 판단하고 영역 개수를 증가시킨다.
            cnt += 1
    else:  # 종료 이벤트인 경우
        stack.pop()
        cnt += 1

print(cnt)