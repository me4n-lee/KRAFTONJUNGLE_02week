#https://www.acmicpc.net/problem/11053
#가장 긴 증가하는 부분 수열
#11053

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n  # dp[i]는 i를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
length = 0  # 현재까지 가장 긴 증가하는 부분 수열의 길이

for i in range(n):
    left, right = 0, length

    while left < right:
        mid = (left + right) // 2
        if dp[mid] < arr[i]:
            left = mid + 1
        else:
            right = mid

    dp[left] = arr[i]

    if left == length:
        length += 1

print(length)