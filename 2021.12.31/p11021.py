import sys

T = int(input())
answer = []

for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    answer.append(a+b)

for i in range(T):
    print('Case #%s: %s'%(i+1, answer[i]))