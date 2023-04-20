#https://www.acmicpc.net/problem/1933
#스카이라인
#1933

n = int(input())
n_list = []
for i in range(n):
    l, h, r = map(int, input().split())
    n_list.append([l,h,r])

print(n_list)

n_list.sort()

print(n_list)

# for i in range(n):
