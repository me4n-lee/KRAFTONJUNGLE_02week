#https://www.acmicpc.net/problem/1715
#카드 정렬하기
#1715

import heapq
import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for i in range(n):
    x = int(input())
    heapq.heappush(n_list, x)

# print(n_list)

# sum_list = []
# k = sum(sum_list)

result = 0

# while len(n_list) > 0:
while len(n_list) > 1: #1개가 남을때까지 반복해야하만 한다. 

#이런 알고리즘을 쓴 이유는, 2개씩 더해갈것이니깐!
#두개를 더한값이 원래 있는 수들보다 작은 2개에 포함된다면 
#그것또한 먼저 계산해야한다. 제일 적은값을 뽑아내는게 맞다.
    a = heapq.heappop(n_list)
    b = heapq.heappop(n_list)

    sum = a + b
    result = result + sum

    heapq.heappush(n_list, sum)

    # print(n_list)

print(result)