import random


def star(n, m):
    x = random.randint(1, 1000)
    if(x > (1000-10*n)):
        return 'success'
    elif(x <= 10*m):
        return 'distroy'
    else:
        return 'fail'


success = [40, 35, 30, 30, 30, 30, 30, 30, 30, 30, 0]
fail = [0.6, 1.3, 1.4, 2.1, 2.1, 2.1, 2.8, 2.8, 7, 7, 0]

x = 0
fail_count = 0
total = 0
star22 = 0
distroy = 0

while(True):
    if(total == 10000):
        break
    result = star(success[x], fail[x])
    if(result == 'success'):
        x = x+1
        print(x+12, '성')
        fail_count = 0
    elif(result == 'fail'):
        if(x == 0 or x == 3 or x == 8):
            print(x+12, '성')
        else:
            fail_count += 1
            x = x-1
            print(x+12, '성')
    elif(result == 'distroy'):
        print('파괴 되었습니다.')
        x = 0
        distroy += 1
        total += 1

    if(x == 10):
        print('========22성 달성=========')
        x = 0
        star22 += 1
        total += 1

    if(fail_count == 2):
        x = x+1
        fail_count = 0
        print(x+12, '성 chance time')

print('성공 :', star22)
print('실패 :', distroy)
