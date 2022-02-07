input = int(input())
change = 1000 - input
array = [500, 100, 50, 10, 5, 1]
count = 0

for i in array:
    count += change//i
    change %= i

print(count)
