#https://www.acmicpc.net/problem/1933
#스카이라인
#1933

import heapq

n = int(input())

full_list = []
n_list = []
for i in range(n):
    l, h, r = map(int, input().split())

    full_list.append([l,h,r])

    n_list.append([l,h])
    n_list.append([r,0])

full_list.sort()

print(full_list)

# print(n_list)

n_list.sort()

print(n_list)

# for i in range(len(n_list)):
    

heap = []

for i in range(n):
    left = n_list[i][0]
    high = n_list[i][1]
    right = n_list[i][2]

    if #만약 라이트가 0이 아니라면
        heapq.heappush(heap, high)
        #힙중에 가장 큰 값을 출력

    else: #만약 라이트가 0이면
        #힙중에 가장 큰 값을 출력

    #만약 라이트까지 온다면 
        heapq.heappop(high)

    