#https://www.acmicpc.net/problem/17608
#막대기
#17608

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
n_list = deque()
for i in range(n):
    a = int(input())
    n_list.appendleft(a)

# print(n_list)

result = []
max_result = 0

for i in range(n):
    # n_list[i] = int(input())
    # if len(result) == 0:
    #     result.append(n_list[i])

    # elif n_list[i] > max(result):
    #     result.append(n_list[i])

    if n_list[i] > max_result:
        result.append(n_list[i])
        max_result = n_list[i]
    

# print(result)

print(len(result))

#세상에. max를 쓰면 시간초과가 나온다 ㅋㅋㅋ

#시간 초과가 발생하는 이유는 max(result) 함수 때문입니다.
#이 함수는 리스트의 최대값을 찾기 위해 매번 전체 리스트를 순회하게 됩니다. 
# 따라서 이 코드는 시간 복잡도가 O(n^2)이 됩니다. 
#이를 개선하기 위해 현재까지 찾은 최대값을 변수에 저장하면 시간 복잡도를 줄일 수 있습니다.