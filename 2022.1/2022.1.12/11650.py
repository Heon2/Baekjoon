import sys
input = sys.stdin.readline

my_list = []
num = int(input())
for i in range(num):
    x, y = map(int, input().split())
    my_list.append([x, y])

my_list.sort()
for i in range(num):
    print(my_list[i][0], my_list[i][1])
