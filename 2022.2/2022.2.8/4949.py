import sys
input = sys.stdin.readline

result = []

while(True):
    str = input()
    stack = []
    if(str[0] == '.'):
        break
    for i in str:
        if(i == '('):
            stack.append(i)
        elif(i == '['):
            stack.append(i)
        if(len(stack) != 0):
            if(i == ')' and stack[-1] == '('):
                stack.pop()
            elif(i == ']' and stack[-1] == '['):
                stack.pop()
            elif(i == ')' and stack[-1] == '['):
                stack = [-1]
                break
            elif(i == ']' and stack[-1] == '('):
                stack = [-1]
                break
        # no일때
        else:
            if(i == ')' or i == ']'):
                stack = [-1]
                break
    if(len(stack) == 0):
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)
