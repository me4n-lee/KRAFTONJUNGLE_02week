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
    n_list.append(x)

heapq.heapify(n_list)

print(n_list)

sum_list = []
k = sum(sum_list)

for i in range(n):
    
    #sum_list의 합을 k에 저장
    # k = sum(sum_list)

    #배열중 최소값을 가져옴
    a = heapq.heappop()

    k = k + a

    sum_list.append(a)


print(k)