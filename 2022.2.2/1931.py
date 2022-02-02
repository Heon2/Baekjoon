import sys
input = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

array_sort = sorted(array, key=lambda x: (x[1], x[0]))

end = array_sort[0][1]
count = 1
for k in range(1, n):
    if(end <= array_sort[k][0]):
        end = array_sort[k][1]
        count += 1


print(count)
