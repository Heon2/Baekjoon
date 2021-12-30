import sys

T  = int(input())
answer = []

for i in range(T):
    A,B = map(int, sys.stdin.readline().split())
    answer.append(A+B)

for i in range(T):
    print(answer[i])