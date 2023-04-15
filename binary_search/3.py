#https://www.acmicpc.net/problem/2110
#공유기 설치
#2110

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
n_list = []
for i in range(n):
    a = int(input())
    n_list.append(a)

# print(n_list)

n_list.sort()

start = 0
end = max(n_list)- min(n_list)
result = 0

# for i in range(c):
# n중에 c만큼을 정할것임
# 그 c들중의 거리차이중 가장 작은것이 최대가 되게끔 하도록 해야함
# 출력은 그 작은것중 최대인것을 출력할예정
while start <= end:
    mid = (start + end) // 2
    # count = 0
    # target = 0    
    count = 1
    target = min(n_list)

    for i in range(n):
        if n_list[i] - target >= mid:
            count = count + 1
            target = n_list[i]

    # if count == c:
    #     result = mid

    # if count > c:
    #     start = mid + 1

    if count >= c:
        result = mid
        start = mid + 1

    elif count < c:
        end = mid - 1
    
    # if n_list[mid] == target:

    # elif n_list[mid] > target:
    #     start = mid +1
    
    # elif n_list[mid] < target:
    #     end = mid + 1

print(result)