#https://www.acmicpc.net/problem/10000
#원 영역
#10000

import sys
input = sys.stdin.readline

n = int(input())
n_list = []
arrange = []
stack = []
for i in range(n):
    x, r = map(int,input().split())
    n_list.append([x,r])

    left = x - r
    right = x + r

    arrange.append((left, 1))  # 원의 왼쪽 경계에 1을 할당하여 시작 이벤트를 나타낸다.
    arrange.append((right, -1))  # 원의 오른쪽 경계에 -1을 할당하여 종료 이벤트를 나타낸다.

arrange.sort()

cnt = 0
open_cnt = 0
for _, event in arrange:
    if event == 1:  # 시작 이벤트인 경우
        if open_cnt == 0:  # 새로운 영역이 시작되므로 영역 개수를 증가시킨다.
            cnt += 1
        open_cnt += 1
    else:  # 종료 이벤트인 경우
        open_cnt -= 1

print(cnt)


#     arrange.append([left, right])

#     # print(arrange)
#     # print(arrange[i])

# arrange.sort()
# # cnt = 1

# for i in range(n):
#     stack.append(arrange[i])
#     #전체 리스트에서 일치하는 점이 1개 있다면? / 
#     #단, 한번 카운트되면 다른 점에 같은 숫자가 있다하더라도 새지 않음
#     if stack == 
#         cnt +=1
#     #전체리스트에서 일치하는점이 2개 있다면?
#     if 
#         cnt +=2
#     #전체리스트에서 일치하는점이 0개 있다면?
#     else:
#         cnt +=1