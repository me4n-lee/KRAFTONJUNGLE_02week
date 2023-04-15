#https://www.acmicpc.net/problem/11053
#가장 긴 증가하는 부분 수열
#11053

n = int(input())
n_list = list(map(int, input().split()))

dp = [0] * n
# print(dp)
for i in range(n):
    for j in range(i):
        if n_list[i] > n_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

    # print(dp)

print(max(dp))