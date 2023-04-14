#이분탐색 / 함수형 / 재귀함수 구현

#arr = 리스트
#key = 탐색하고싶은 값
#start, end
def binary(arr, key, start, end):

    mid = (start + end) // 2

    if start > end:
        return None

    if arr[mid] == key:
        return mid
    
    elif arr[mid] > key:
        return binary(arr, key, start, mid - 1)
    
    elif arr[mid] < key:
        return binary(arr, key, mid + 1, end)

#target = 찾고자 하는 값을 입력받기위함
n , target = list(map(int, input().split()))
n_list = list(map(int, input().split()))

#이분탐색은 항상 정렬된 배열에서만 적용 가능하다
n_list.sort()

result = binary(n_list, target, 0, n-1)

print(result)