#https://www.acmicpc.net/problem/5904
#Moo 게임
#5904

import sys
input = sys.stdin.readline

n = int(input())

#재귀적 표현이 아닌 반복문으로 풀이하는법

#k 가 0 일때 len은 3 / 초기값
k = 0
length_list = [3]

while length_list[-1] < n:
    k += 1
    next_length = length_list[-1] + 1 + k + 2 + length_list[-1]
    length_list.append(next_length)

def fun(n, k, length_list):

    #탈출조건
    if k == 0:
        if n == 1:
            return "m"
        elif n == 2:
            return "o"
        elif n == 3:
            return "o"

    #첫번째 s(k-1)에 위차할경우
    if n <= length_list[k - 1]:
        return fun(n, k - 1, length_list)
    
    #가운데 1+ k+2 구간에 위치할경우
    elif n == length_list[k - 1] + 1:
        return "m"
    elif n <= length_list[k - 1] + k + 3:
        return "o"
    
    #두번째 s(k-1) 에 위치할경우
    else:
        return fun(n - (length_list[k - 1] + k + 3), k - 1, length_list)


print(fun(n, k, length_list))