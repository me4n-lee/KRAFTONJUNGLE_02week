#https://www.acmicpc.net/problem/9012
#괄호
#9012

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a = list(input().strip())
    t_list = []
    valid = True
    # print(a)

    for i in range(len(a)):
        if a[i] == "(":
            t_list.append(a[i])

        else:
            if len(t_list) != 0:
                t_list.pop()
            else:
                valid = False
                break
    
    if valid and len(t_list) == 0:
        print("YES")
    
    else:
        print("NO")

#valid를 어떻게 생각해 냈는지? 아니면 다른 방법으로 풀수 있는지