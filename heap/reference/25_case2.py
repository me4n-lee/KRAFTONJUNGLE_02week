#https://www.acmicpc.net/problem/1655
#가운데를 말해요
#1655

import heapq
import sys
input = sys.stdin.readline

n= int(input())

left_heap = []
right_heap = []

for i in range(n):
    a = int(input())

    if(len(left_heap)) == (len(right_heap)):
        heapq.heappush(left_heap, -a)

    else:
        heapq.heappush(right_heap, -a)

    # 양쪽 heap에 요소들이 존재한다면,
    # leftheap의 루트에 음수를 곱한 값이 rightheap의 루트보다 크다면        
    if len(left_heap) >= 1 and len(right_heap) >= 1 and -left_heap[0] > right_heap[0]:
        max_left = heapq.heappop(left_heap) * -1
        min_right = heapq.heappop(right_heap)

        heapq.heappush(left_heap, min_right * -1)
        heapq.heappush(right_heap, max_left)

    print(left_heap[0] * -1)