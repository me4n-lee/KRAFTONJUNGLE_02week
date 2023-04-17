#https://www.acmicpc.net/problem/2812
#크게 만들기
#2812

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_list = list(input().strip())

#이문제에서 제일 많이 해맨부분 
k_first = k

# print(n_list)
stack = []
# stack = deque()
# deque객체에서는 슬라이싱을 지원하지 않고있다.

for i in range(n):
    while k > 0 and stack and stack[-1] < n_list[i]:
        stack.pop()
        k -= 1
    stack.append(n_list[i])

print(''.join(stack[:n-k_first]))

#결과값 출력에 사용된 join() 함수는 리스트안에 있는 문자를 문자열로 바꾸어주는 함수입니다.
#https://jokerldg.github.io/algorithm/2021/05/25/make-big.html