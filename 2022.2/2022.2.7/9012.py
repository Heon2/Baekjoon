import sys
input = sys.stdin.readline

n = int(input())
result = []
count = 0
for i in range(n):
    k = input()
    count = 0
    for j in k:
        if(j == ")" and count == 0):
            count = -1  # NO를 출력하기위해
            break
        if(j == "("):
            count += 1
        elif(j == ")"):
            count -= 1
    if(count == 0):
        result.append('YES')
    else:
        result.append('NO')

for i in result:
    print(i)
