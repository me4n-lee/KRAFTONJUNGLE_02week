import sys
from itertools import combinations

input = sys.stdin.readline

n, c = map(int, input().split())
n_list = []
for i in range(n):
    a = int(input())
    n_list.append(a)

n_list.sort()

def min_distance(combination):
    min_dist = float('inf')
    for i in range(1, len(combination)):
        distance = combination[i] - combination[i - 1]
        if distance < min_dist:
            min_dist = distance
    return min_dist

max_min_distance = 0
for combination in combinations(n_list, c):
    min_dist = min_distance(combination)
    if min_dist > max_min_distance:
        max_min_distance = min_dist

print(max_min_distance)