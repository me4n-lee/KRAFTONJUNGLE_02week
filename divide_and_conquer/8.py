#https://www.acmicpc.net/problem/1629
#곱셈
#1629

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def fun(a, b, c):

    # result = fun(a, b//2, c)

    if b == 1:
        return a % c
    
    elif b % 2 == 0:
        result = fun(a, b//2, c)
        return (result * result) % c

    else:
        result = fun(a, b//2, c)
        return (result * result * a) % c
    

print(fun(a,b,c))