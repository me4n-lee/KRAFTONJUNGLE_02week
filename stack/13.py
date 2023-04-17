#https://www.acmicpc.net/problem/10773
#제로
#10773

# from collections import deque
import sys
input = sys.stdin.readline

n_list = []
n = int(input())
for i in range(n):
    a = int(input())

    if a > 0:
        n_list.append(a)
    
    if a == 0:
        n_list.pop()

#     n_list.append(a)

# for i in range(n):

#     if n_list[i]:

print(sum(n_list))