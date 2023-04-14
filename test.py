n, m = map(int, input().split())
n_list = list(map(int, input().split()))

start = 0
end = max(n_list)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in range(n):
        if n_list[i] > mid:
            total += n_list[i] - mid

    if total == m:
        result = mid
        break

    elif total > m:
        start = mid + 1

    elif total < m:
        end = mid - 1

print(result)