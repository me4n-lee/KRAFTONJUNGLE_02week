#https://www.acmicpc.net/problem/3190
#뱀
#3190

from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) #보드의 크기
k = int(input()) #사과 개수
k_list = deque() #사과의 위치
for i in range(k):
    a, b = map(int, input().split())
    k_list.append([b,a]) # 행, 열 일치를 시켜줘야하는데.. 아래 코드들이 열 행이다.

# print(k_list)

l = int(input()) # 뱀의 방향전환 정보
l_list = deque()
for i in range(l):
    x, c = input().split()
    l_list.append([int(x),c])

# print(l_list[1][0])

# D일때 오른쪽으로 머리돌림
# L일때 왼쪽으로 머리돌림
time = 0
snake = deque([[1,1]])
#뱀은 0,0에서부터 시작함
#처음은 오른쪽으로 머리를 향함


direction_idx = 0
# 이동 방향 설정
dx = [1, 0, -1, 0] # 우, 하, 좌, 상
dy = [0, 1, 0, -1] # 우, 하, 좌, 상

while True:

    time += 1
    #뱀의 머리위치
    head_x, head_y = snake[-1] # 뱀의 머리위치!

    #뱀의 이동
    next_x = head_x + dx[direction_idx]
    next_y = head_y + dy[direction_idx]

    #벽에 부딪히면 종료
    if not(1 <= next_x <= n) or not(1 <= next_y <= n):
        break
    
    #뱀의 머리가 자기 몸과 부딪히면 종료
    if [next_x, next_y] in snake:
        break

    #뱀의 머리를 덱에 추가
    snake.append([next_x, next_y])

    #사과가 있는 위치면 사과를 덱에서 삭제
    #사과가 없는 위치면 꼬리를 없앤다
    if [next_x, next_y] in k_list:
        k_list.remove([next_x, next_y])
    else:
        snake.popleft()

    #만약 타임이 l_list와 일치하게 된다면 방향을 바꾸어 줘야함 
    # D일때 오른쪽으로 머리돌림
    # L일때 왼쪽으로 머리돌림
    if l_list and time == l_list[0][0]:
        _, direction = l_list.popleft()
        if direction == 'D':
            direction_idx = (direction_idx + 1) % 4
        else: # direaction == 'C'
            direction_idx = (direction_idx - 1) % 4

print(time)