#https://www.acmicpc.net/problem/10828
#스택
#10828

import sys
input = sys.stdin.readline

n_list = []

n = int(input())

for i in range(n):
    
    a = input().split()
    # print(a)
    
    if a[0] =='top':
        # n_list.top()
        if len(n_list) == 0:
            print(-1)
        else:
            print(n_list[-1])

    elif a[0] =='size':
        # n_list.size()
        print(len(n_list))
    
    elif a[0] =='pop':
        # n_list.pop()
        if len(n_list) == 0:
            print(-1)
        else:
            print(n_list.pop())

    elif a[0] =='empty':
        # n_list.empty()
        if len(n_list) == 0:
            print(1)
        else:
            print(0)

    #push()
    else:
        n_list.append(a[1])

    

# print(n_list)
