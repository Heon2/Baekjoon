n = int(input())
array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append([y, x])

array_sort = sorted(array)

for y, x in array_sort:
    print(x, y)
