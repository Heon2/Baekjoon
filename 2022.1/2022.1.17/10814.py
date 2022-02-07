import sys
num = int(input())
array = []

for i in range(num):
    age, name = sys.stdin.readline().split()

    array.append((int(age), i, name))

array.sort()
for age, order, name in array:
    print(age, name)
