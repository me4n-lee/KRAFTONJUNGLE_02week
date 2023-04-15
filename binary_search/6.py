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

m_list.sort()

catch = 0

for i in range(n):
    x, y = n_list[i]
    start = 0
    end = m - 1

    while start <= end:
        mid = (start + end) // 2
        dist = abs(m_list[mid] - x) + y

        if dist <= l:
            catch += 1
            break
        elif m_list[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

print(catch)

        