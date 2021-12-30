num = int(input())
answer = []
for i in range(num):
    str = input().split(' ')
    A = int(str[0])
    B = int(str[1])
    answer.append(A+B)

for i in range(num):
    print(answer[i])
