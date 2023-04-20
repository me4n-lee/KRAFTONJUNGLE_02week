#https://www.acmicpc.net/problem/5904
#Moo 게임
#5904

import sys
input = sys.stdin.readline

n = int(input())

# n_3 = (n + 1) % 3 

# if n_3 == 0:
#     print("m")
# elif n_3 == 1:
#     print("o")
# else:
#     print("o")

        # fun(n, k+1) + 1 + n+2 + fun(n, k+1)

def n_length(k):
    if k == 0:
        return 3
    else:
        return (n_length(k-1) + 1 + k+2 + n_length(k-1))

# def fun(n,k):
#     if n == 1:
#         result = "m"
#     elif n == 2:
#         result = "o"
#     elif n == 3:
#         result = "o"
#     else:

def fun(n, k):
    if k == 0:
        if n == 1:
            return "m"
        elif n == 2:
            return "o"
        elif n == 3:
            return "o"

    #첫번째 s(k-1)에 위치할때
    if n <= n_length(k - 1):
        return fun(n, k - 1)
    
    # 1+ k+2 구간에 위치할때
    elif n == n_length(k - 1) + 1: # s(k-1)
        return "m"
    elif n <= n_length(k - 1) + k + 3:
        return "o"
    
    #두번째 s(k-1)에 위치할때
    else:
        return fun(n - (n_length(k - 1) + k + 3), k - 1)

k = 0
while n_length(k) < n:
    k += 1

print(fun(n,k))