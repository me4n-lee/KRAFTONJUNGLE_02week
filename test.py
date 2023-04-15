import sys
# input = sys.stdin.readline  # 주석 처리하여 테스트에 사용할 수 있도록 함

m, n, l = map(int, input().split())
m_list = list(map(int, input().split()))

n_list = []
for i in range(n):
    x = list(map(int, input().split()))
    n_list.append(x)

m_list.sort()
catch = 0

new_n_list = [n_list[i].copy() for i in range(n)]

for i in range(m):
    for j in range(n):
        new_n_list[j][0] = n_list[j][0] - m_list[i]

    plus_list = []
    for j in range(n):
        alpa = abs(new_n_list[j][0]) + abs(new_n_list[j][1])
        plus_list.append(alpa)
    
    plus_list.sort()
    
    for j in range(n):
        if plus_list[j] > l:
            break
        if plus_list[j] <= l and catch == 0:
            catch += 1

print(catch)