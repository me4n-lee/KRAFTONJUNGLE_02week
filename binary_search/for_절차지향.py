#이분탐색 / 함수형 / 반복문 구현

# #arr = 리스트
# #key = 탐색하고싶은 값
# #start, end
# def binary(arr, key, start, end):
#     while start <= end:
#         mid = (start + end) // 2

#         if arr[mid] == key:
#             return mid
        
#         elif arr[mid] > key:
#             end = mid - 1

#         elif arr[mid] < key:
#             start = mid + 1
    
#     return None

# #target = 찾고자 하는 값을 입력받기위함
# n , target = list(map(int, input().split()))
# n_list = list(map(int, input().split()))
# #이분탐색은 항상 정렬된 배열에서만 적용 가능하다
# n_list.sort()

# result = binary(n_list, target, 0, n-1)

# print(result)

#target = 찾고자 하는 값을 입력받기위함
n , target = list(map(int, input().split()))
n_list = list(map(int, input().split()))
#이분탐색은 항상 정렬된 배열에서만 적용 가능하다
n_list.sort()

start = 0
end = n - 1
ans = 0

while start <= end:
    mid = (start + end) // 2

    if n_list[mid] == target:
        ans = mid
        break

    elif n_list[mid] > target:
        end = mid - 1
    
    elif n_list[mid] < target:
        start = mid + 1

print(ans)