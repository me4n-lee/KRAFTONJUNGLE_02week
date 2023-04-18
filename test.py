import sys

input = sys.stdin.readline

n = int(input())
arrange = []
for i in range(n):
    x, r = map(int, input().split())

    left = x - r
    right = x + r

    arrange.append([left, right])

# Sort the list based on the left coordinate
arrange.sort(key=lambda x: x[0])

stack = set()
cnt = 1

for i in range(n):
    left_now = arrange[i][0]
    right_now = arrange[i][1]

    # Check if left_now and right_now are in the stack
    left_in_stack = left_now in stack
    right_in_stack = right_now in stack

    # If both left_now and right_now are in the stack
    if left_in_stack and right_in_stack:
        cnt += 2
    else:
        cnt += 1

    stack.add(left_now)
    stack.add(right_now)

print(cnt)