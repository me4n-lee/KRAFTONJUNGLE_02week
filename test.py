import sys
input = sys.stdin.readline

n = int(input())
n_list = []
arrange = []
for i in range(n):
    x, r = map(int, input().split())
    n_list.append([x, r])

    left = x - r
    right = x + r

    arrange.append([left, right])

arrange.sort()

cnt = 0
stack = []
for i in range(n):
    while stack and stack[-1][1] < arrange[i][0]:  # 스택의 마지막 원소의 오른쪽 경계가 현재 원의 왼쪽 경계보다 작으면 겹치지 않는 영역이므로 스택에서 원소를 제거한다.
        stack.pop()
    
    if not stack:  # 스택이 비어있으면 새로운 영역이 시작되므로 영역 개수를 증가시킨다.
        cnt += 1
    else:  # 스택에 원소가 있는 경우, 원들의 경계가 겹치는지 확인한다.
        overlap_cnt = 0
        for j in range(len(stack)):
            if stack[j][1] == arrange[i][0]:  # 겹치는 점이 1개 있는 경우
                overlap_cnt += 1
            elif stack[j][1] > arrange[i][0]:  # 겹치는 점이 2개 있는 경우
                overlap_cnt += 2
                break
        
        cnt += overlap_cnt

    stack.append(arrange[i])

print(cnt)