#https://www.acmicpc.net/problem/8983
#사냥꾼
#8983

import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
m_list = list(map(int, input().split()))

n_list = []
for i in range(n):
    x = list(map(int, input().split()))
    n_list.append(x)

#print(m_list)
#print(n_list)

sum_list = []
for i in range(n):
    a = sum(n_list[i])
    sum_list.append(a)
#print(sum_list)

catch = [0] * n
# print(sum_list)

#새로운 배열을 복사해서 사용
new_n_list = [n_list[i].copy() for i in range(n)]

# minus_list = [0] * n
# n = 동물의 수 m= 사대의 수 l = 사정거리
for i in range(m):
    for j in range(n):
        new_n_list[j][0] = n_list[j][0] - m_list[i]

    print(new_n_list)

    plus_list = []
    for j in range(n):
        alpa = abs(new_n_list[j][0]) + abs(new_n_list[j][1])
        plus_list.append(alpa)
    
    plus_list.sort()
    print(plus_list)

    for j in range(n):
        if plus_list[j] > l:
            break
        if plus_list[j] <= l and catch == 0:
            catch += 1

print(catch)