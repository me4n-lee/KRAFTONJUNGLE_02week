#https://www.acmicpc.net/problem/2630
#색종이 만들기
#2630

import sys
input = sys.stdin.readline

#하얀색 색종이 / 파란색 색종이
white = 0
blue = 0

n = int(input())
n_list = []
for i in range(n):
    a = list(map(int, input().split()))
    n_list.append(a)

# print(n_list)

# width = n
# hight = n    

def fun(x,y,n):
    global white, blue

    color = n_list[x][y] # 처음 위치를 가져와서 그 색을 기존색으로 정함

    #나머지가 맞는지 if문을 돌리고 아니면 함수 호출
    for i in range(n):
        for j in range(n):
            if n_list[x + i][y + j] != color:
                fun(x, y, n//2) # 1사분면
                fun(x, y + n//2, n//2) #2 사분면
                fun(x + n//2, y, n//2) #3 사분면
                fun(x + n//2, y + n//2, n//2) #4 사분면
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1

fun(0, 0, n)

print(white)
print(blue)


    # for i in range(x, x+n):
    #     for j in range(y, y+n):
    #         if color != paper[i][j]: