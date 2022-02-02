n = int(input())
array = list(map(int, input().split()))
array_sort = sorted(array)

result = 0
sum = 0

for i in array_sort:
    sum += i
    result += sum

print(result)
