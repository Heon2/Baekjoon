import sys
input = sys.stdin.readline

n = int(input())
array = []
result = []
for i in range(n):
    command = input()
    if(command.startswith('push')):
        a, b = command.split()
        array.append(int(b))
    if(command.startswith('top')):
        if(len(array) == 0):
            result.append(-1)
        else:
            result.append(array[-1])
    if(command.startswith('size')):
        result.append(len(array))
    if(command.startswith('empty')):
        if(len(array) == 0):
            result.append(1)
        else:
            result.append(0)
    if(command.startswith('pop')):
        if(len(array) == 0):
            result.append(-1)
        else:
            result.append(array.pop())

for i in result:
    print(i)
