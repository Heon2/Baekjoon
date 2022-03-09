n = int(input())
count = 0


def sosu(x):
    if(x == 1):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True


array = list(map(int, input().split()))
for i in array:
    if(sosu(i) == True):
        count += 1

print(count)
