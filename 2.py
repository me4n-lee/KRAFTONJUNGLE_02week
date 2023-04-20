#https://www.acmicpc.net/problem/16120
#PPAP
#16120

n_list = list(input())

# print(n_list)

stack = []

# for i in range(len(n_list)):

#     if len(n_list) == 0:
#         print("PPAP")

#     if n_list[i] == "P":
#         if n_list[i] == n_list[-1]:
#             print("PPAP")

#     if n_list[i] == "A":

for i in range(len(n_list)):
    stack.append(n_list[i])
    
    if len(stack) >= 4 and "".join(stack[-4:]) == "PPAP":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append("P")

if len(stack) == 1 and stack[0] == "P":
    print("PPAP")
else:
    print("NP")

# for _ in range(len(stack) - 3):
#     if stack[-1] == "P" and stack[-2] == "A" and stack[-3] == "P" and stack[-4] == "P":
#         stack.pop()
#         stack.pop()
#         stack.pop()
#         stack.pop()
#         stack.append("P")
#         break

# result = [n_list[i] + n_list[i+1] for i in range(0, len(n_list)-1, 2)]
# if len(n_list) % 2 == 1:
#     result.append(n_list[-1])        

#     # if len(n_list) == 0:

#     if n_list[i] == "PP":
#         stack.append(n_list[i])
#     elif n_list[i] == "PA":

#     elif n_list[i] == "AP":
#         if stack[i-1] == "PP"
#         stack.pop(n_list[i])
    
#     elif n_list[i] == "AA":

#     elif n_list[i] == "A":
#         print("NP")
#     elif n_list[i] == "P":
#         if n_list[i] == n_list[-1]:
#             print("PP")
        


