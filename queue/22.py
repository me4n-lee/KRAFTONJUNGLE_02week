#https://www.acmicpc.net/problem/11866
#요세푸스 문제 0
#11866

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_list = deque()

for i in range(n):
    n_list.append(i+1)

print(n_list)
result = []
while len(n_list) > 0:
    for i in range(k-1):
        n_list.append(n_list.popleft())
    result.append(str(n_list.popleft()))

    print(n_list)
    print(result)

print("<", end ="")

for i in range(len(result)):
    print(result[i] + ",", end ="")
    
print(">", end ="")
        

