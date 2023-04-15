#https://www.acmicpc.net/problem/2470
#두 용액
#2470

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

# print(n_list)

n_list.sort()

# print(n_list)

start = 0
#end = n
end = n - 1
min_target = float('inf')

while start <= end:
    mid = (start + end) // 2
    
    for i in range(n):
        chai = abs(n_list[mid] + n_list[i])
        if min_target > chai:
            min_target = chai
            a = n_list[mid]
            b = n_list[i]
    # for i in

    # if min_target >= 0:
    # if min_target > 0:
    #     start = mid + 1

    # elif min_target < 0:
    #     end = mid - 1

    if min_target > 0:
        start = mid + 1

    elif min_target < 0:
        end = mid - 1

print(a, b)
# print(result) 
