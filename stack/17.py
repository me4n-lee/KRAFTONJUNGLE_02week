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

    arrange.append([left, right])

    # print(arrange)
    # print(arrange[i])

arrange.sort()
# cnt = 1

for i in range(n):
    stack.append(arrange[i])
    #전체 리스트에서 일치하는 점이 1개 있다면? / 
    #단, 한번 카운트되면 다른 점에 같은 숫자가 있다하더라도 새지 않음
    if stack == 
        cnt +=1
    #전체리스트에서 일치하는점이 2개 있다면?
    if 
        cnt +=2
    #전체리스트에서 일치하는점이 0개 있다면?
    else:
        cnt +=1