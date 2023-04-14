#https://www.acmicpc.net/problem/1920
#수 찾기
#1920

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# print(n_list)
# print(m_list)

n_list.sort()
ans = [0] * m

for i in range(m):
    target = m_list[i]
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if target == n_list[mid]:
            ans[i] = 1
            break

        elif target < n_list[mid]:
            end = mid - 1

        elif target > n_list[mid]:
            start = mid + 1

# print(ans)

for i in range(len(ans)):
    print(ans[i])