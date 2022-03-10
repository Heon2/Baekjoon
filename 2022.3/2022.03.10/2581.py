m = int(input())
n = int(input())

array = []


def sosu(x):
    if(x == 1):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True


for i in range(m, n+1):
    if(sosu(i) == True):
        array.append(i)

if(len(array) == 0):
    print(-1)
else:
    print(sum(array))
    print(min(array))
