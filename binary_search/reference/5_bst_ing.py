#https://www.acmicpc.net/problem/11053
#가장 긴 증가하는 부분 수열
#11053

import sys
input = sys.stdin.readline 

a = int(input())
a_list = list(map(int, input().split()))

# print(a_list)

start = 0
end = len(a_list) - 1

while start <= end:
    mid = (start + end) // 2
    count = 1
    max_count = a

    if a_list[mid] > a_list[start]:
        count += 1
        start += 1

    if a_list[mid] > a_list[end]:
        count += 1
        end += 1     

    if count > max_count:
        max_count = count

print(max_count)
        

