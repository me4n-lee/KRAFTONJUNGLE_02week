#이분탐색 / 절차지향 / 반복문 구현

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