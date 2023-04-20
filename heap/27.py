#https://www.acmicpc.net/problem/13334
#철로
#13334

import sys
import heapq

input = sys.stdin.readline

n = int(input())
n_list = []
for i in range(n):
    h, o = map(int, input().split())
    n_list.append((min(h, o), max(h, o)))

d = int(input())

#x[1]을 기준으로 정렬하겠다.
n_list.sort(key=lambda x: x[1])

# print(n_list)
count = 0
pq = []

#start = h / end = o 값
for i in range(n):
    start, end = n_list[i]

    if end - start <= d:
        heapq.heappush(pq, start)

    while pq and pq[0] < end - d:
        heapq.heappop(pq)

    count = max(count, len(pq))

print(count)

# for i in startend:
#     if i[1] - i[0] <= d:
#         abileroute.append(i)

#
