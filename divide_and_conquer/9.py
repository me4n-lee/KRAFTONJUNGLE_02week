#https://www.acmicpc.net/problem/6549
#히스토그램에서 가장 큰 직사각형
#6549

import sys
input = sys.stdin.readline

get_list = list(map(int,input().split()))
n = get_list[0]
n_list = get_list[1:]

print(n)
print(n_list)

# for _ in range(n):
#     n = list(map(int,input()))


result = 0

def fun(i):
    global result
    
    now = n_list[i]
    next = n_list[i+1]

    result = max(result, n_list[i])

    if n_list[i] == n_list[-1]:
        return result

    if next >= now:
        result = result + now
        return fun(i+1)
    
    if next < now:
        return fun(i+1)

fun(0)
print(result)
