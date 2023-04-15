import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()

min_target = float('inf')
a, b = 0, 0

start = 0
end = n - 1

while start < end:
    s = n_list[start] + n_list[end]
    if abs(s) < min_target:
        min_target = abs(s)
        a, b = n_list[start], n_list[end]
        
    if s > 0:
        end -= 1
    else:
        start += 1

print(a, b)

#위 코드는 투포인터 방식으로 작성된 코드입니다.
# start와 end 변수를 각각 첫 번째 용액과 마지막 용액의 인덱스로 초기화한 후, 
# 반복문을 돌면서 두 용액의 합을 계산하고, 
# 그 합의 절댓값이 현재까지의 최소 차이값보다 작으면 
# 최소 차이값과 그 때의 두 용액 값을 업데이트합니다. 
# 그리고 두 용액의 합이 0보다 크면 end 변수를 하나 줄이고, 
# 0보다 작으면 start 변수를 하나 늘려나가면서 최소 차이값을 찾아냅니다.