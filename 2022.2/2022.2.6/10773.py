import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    k = int(input())
    if(k == 0):
        if(len(array) != 0):
            array.pop()
    else:
        array.append(k)

print(sum(array))
