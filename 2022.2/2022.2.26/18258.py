from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deq = deque()

for i in range(n):
    st = input().split()
    if(st[0] == 'push'):
        deq.append(st[1])
    elif(st[0] == 'pop'):
        if not deq:
            print("-1")
        else:
            print(deq.popleft())
    elif(st[0] == 'size'):
        print(len(deq))
    elif(st[0] == 'empty'):
        if not deq:
            print('1')
        else:
            print('0')
    elif(st[0] == 'front'):
        if not deq:
            print('-1')
        else:
            print(deq[0])
    elif(st[0] == 'back'):
        if not deq:
            print('-1')
        else:
            print(deq[-1])
