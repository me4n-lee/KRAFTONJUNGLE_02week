#https://www.acmicpc.net/problem/11279
#최대 힙
#11279

import heapq
import sys
input = sys.stdin.readline

n = int(input())
x_list = []
for i in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(x_list, -x)

    else:
        if x_list:
            print(-heapq.heappop(x_list))
        else:
            print(0)

#Python의 heapq 라이브러리는 최소 힙(min heap)만 지원하기 때문에, 
# 값을 추가하기 전에 부호를 바꾸고(heapq.heappush(x_list, -x)) 
# 힙에서 값을 꺼낸 후에 부호를 다시 바꿔 원래 값(-heapq.heappop(x_list))을 
# 얻는 방식으로 최대 힙(max heap)을 구현할 수 있습니다.