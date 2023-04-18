#https://www.acmicpc.net/problem/1655
#가운데를 말해요
#1655

import heapq
import sys
input =sys.stdin.readline

n = int(input())

left_heap = []
right_heap = []

for i in range(n):
    a = int(input().strip())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -a)
    else:
        heapq.heappush(right_heap, a)

    if right_heap and -left_heap[0] > right_heap[0]:
        max_left = -heapq.heappop(left_heap)
        min_right = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -min_right)
        heapq.heappush(right_heap, max_left)

    print(-left_heap[0])