#https://www.acmicpc.net/problem/10830
#행렬 제곱
#10830

import sys
input = sys.stdin.readline

n, b = map(int, input().split())
b = int(b)
a_list = []
for i in range(n):
    a = list(map(int, input().split()))
    a_list.append(a)

# print(a_list)

def mult(A, B):
    result = [[0] * (len(B[0])) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= 1000
    return result

# print(mult(a_list, a_list))

def fun(a_list, b):

    if b == 0:
        # return the identity matrix
        return [[int(i == j) for j in range(n)] for i in range(n)]

    if b == 1:
        return a_list
    
    elif b % 2 == 0:
        result = fun(a_list, b//2)
        return mult(result,result)

    else:
        result = fun(a_list, b//2)
        return mult(mult(result,result), a_list)
    
result = fun(a_list, b)

for i in range(n):
    for j in range(n):
        print(result[i][j], end= " ")
    print()
