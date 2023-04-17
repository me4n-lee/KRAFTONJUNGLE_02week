#https://www.acmicpc.net/problem/17608
#막대기
#17608

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
n_list = deque()
for i in range(n):
    a = int(input())
    n_list.appendleft(a)

# print(n_list)

result = []

for i in range(n):
    # n_list[i] = int(input())
    if len(result) == 0:
        result.append(n_list[i])

    elif n_list[i] > max(result):
        result.append(n_list[i])
    

# print(result)

print(len(result))