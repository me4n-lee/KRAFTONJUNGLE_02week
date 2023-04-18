#https://www.acmicpc.net/problem/13334
#철로
#13334

import heapq
import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for i in range(n):
    h, o = map(int, input().split())
    n_list.append([h,o])

d = int(input())

n_list.sort()

print(n_list)
# print(min(n_list)

# print(heapq.heappop(n_list))

now_count = 0

for i in range(len(n_list)):

    target_start = i
    target_end = target_start + d

    print(target_start)
    print(target_end)

    for j in range(len(n_list)):
        count = 0
        
        if target_start >= n_list[j][0] and target_end <= n_list[j][1]:
            count += 1
        else:
            break

        result = max(count, now_count)

        now_count = count

        print(result)

print(result)

    
#이 코드는 여전히 문제의 요구 사항을 정확하게 충족하지 않습니다. 주요 문제점은 다음과 같습니다:

#1. n_list를 정렬하지 않고 시작하므로 각각의 철로의 위치를 올바르게 고려하지 않습니다.
#2. count 변수가 이중 반복문 안에서 초기화되지 않아, 
# 이전 철로 위치에 대한 카운트가 현재 철로 위치의 카운트에 누적됩니다.
#3. 이중 반복문을 사용하여 모든 가능한 철로 위치를 확인하는 것이 아니라, 
# 철로의 왼쪽 끝을 각 사무실의 위치로만 설정합니다. 
# 따라서 다른 가능한 철로 위치를 고려하지 못할 수 있습니다.

# 이러한 문제점들로 인해 이 코드는 문제의 요구 사항을 정확하게 충족하지 않습니다. 
# 이전에 제시한 코드를 사용하시면 문제를 올바르게 해결할 수 있습니다. 
# 아래 코드를 다시 참조하시기 바랍니다.

#철로의 왼쪽 끝을 각 사무실의 위치로만 설정하는 대신, target_start = i로 설정합니다. 
# 이렇게 하면 철로의 위치를 올바르게 고려하지 못할 수 있습니다.