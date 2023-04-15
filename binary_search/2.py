#https://www.acmicpc.net/problem/2805
#나무 자르기
#2805

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# def binary(arr, target, start, end):

#     while start <= end:
#         mid = (start+ mid) // 2

#         if arr[mid] == target:
#             return mid
        
#         elif arr[mid] > target:
#             end = mid - 1

#         elif arr[mid] < target:
#             start = mid + 1
    
#     return None

# for i in range(n):
#     k = n_list[i] - target#자르는 높이
#     chai_list.append(k)

start = 0
end = max(n_list)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in range(n):
        chai = n_list[i] - mid
        if chai > 0:
            total = total + chai

    # if total == m:
    #     result = mid
    #     break

    # elif total > m:
    #     start = mid + 1

    #적어도 m이상이라는 조건을 만족하기 위한 알고리즘!
    #왜 m 이상일까?
    if total >= m:
        result = mid
        start = mid + 1
    
    elif total < m:
        end = mid - 1

print(result)

#     if n_list[mid] == target:
#         ans[i] = n_list[i] -
#         #자르는 높이를 여기서 출력해야하는데 뭐랑 같아질때 출력해야하지?
#         #각각의 나무들을 자른뒤의 나머지값들을 합친게 m이랑 같아질때


#     elif n_list[mid] < target:
#         start = mid + 1

#     elif n_list[mid] > target:
#         end = mid -1

# for i in range(n):
#     k = n_list[i] - target#자르는 높이
#     chai_list.append(k)

# result = sum(chai_list)

# if result == m:
#     print(target)