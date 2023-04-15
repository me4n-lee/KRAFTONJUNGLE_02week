import sys

input = sys.stdin.readline 

n = int(input())
arr = list(map(int, input().split()))

result = [1] * n
for i in range(1, n):
    left, right = 0, i - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < arr[i]:
            left = mid + 1
        else:
            right = mid - 1
    result[i] = max(result[j] for j in range(i) if arr[j] < arr[i]) + 1

print(max(result))