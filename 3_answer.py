#https://www.acmicpc.net/problem/1933
#스카이라인
#1933

import heapq
import sys
input = sys.stdin.readline

n = int(input())

n_list = []
for i in range(n):
    l, h, r = map(int, input().split())

    n_list.append([l, h, r])
    n_list.append([r, -h, r])

n_list.sort(key=lambda x: (x[0], -x[1]))

# heap = [(0, float('inf'))]  # Initialize heap with a dummy building of height 0 and infinite right position
# heapq.heapify(heap)

heap = [(0,0)]
heapq.heapify(heap)
skyline = []

for event in n_list:
    left, height, right = event

    if height > 0:  # If it's a left edge, add the building to the heap
        heapq.heappush(heap, (-height, right))
    else:  # If it's a right edge, remove the building from the heap
        while heap and heap[0][1] <= left:
            heapq.heappop(heap)

    # If the current highest building has changed, add the current position and height to the skyline
    if not skyline or skyline[-1][1] != -heap[0][0]:
        skyline.append((left, -heap[0][0]))

for point in skyline:
    print(point[0], point[1], end=' ')
print()