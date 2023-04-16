import sys
input = sys.stdin.readline

n_list = []

n = int(input())

for i in range(n):
    
    a = input().split()
    
    if a[0] =='top':
        if len(n_list) == 0:
            print(-1)
        else:
            print(n_list[-1])

    elif a[0] =='size':
        print(len(n_list))
    
    elif a[0] =='pop':
        if len(n_list) == 0:
            print(-1)
        else:
            print(n_list.pop())

    elif a[0] =='empty':
        if len(n_list) == 0:
            print(1)
        else:
            print(0)

    else:
        n_list.append(a[1])