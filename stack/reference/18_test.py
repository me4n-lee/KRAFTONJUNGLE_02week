import sys
input = sys.stdin.readline

a_list = list(input().strip())

stack = []
valid = True
for i in range(len(a_list)):
    if a_list[i] == "(" or a_list[i] == "[":
        stack.append(a_list[i])

    elif a_list[i] == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            stack.append(2)
        elif len(stack) >= 2 and stack[-1] == 2 and stack[-2] == "(":
            stack.pop()
            stack.pop()
            stack.append(4)
        else:
            valid = False
            break

    elif a_list[i] == "]":
        if stack and stack[-1] == "[":
            stack.pop()
            stack.append(3)
        elif len(stack) >= 2 and stack[-1] == 3 and stack[-2] == "[":
            stack.pop()
            stack.pop()
            stack.append(9)
        else:
            valid = False
            break

    if len(stack) >= 2 and (isinstance(stack[-1], int) and isinstance(stack[-2], int)):
        stack[-2] += stack[-1]
        stack.pop()

if valid and len(stack) == 1 and isinstance(stack[0], int):
    print(stack[0])
else:
    print(0)