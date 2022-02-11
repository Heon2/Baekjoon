num = 1
result = []

for i in range(3):
    num *= int(input())

string = str(num)
for i in range(10):
    print(string.count(str(i)))
