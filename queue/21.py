#https://www.acmicpc.net/problem/2164
#카드2
#2164

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
n_list = deque()

for i in range(n):
    n_list.append(i+1)

# print(n_list)

while len(n_list) > 1 :
    n_list.popleft()
    n_list.append(n_list.popleft())
    # print(n_list)

print(sum(n_list))

