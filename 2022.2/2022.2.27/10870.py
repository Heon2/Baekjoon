array = [0]*21
array[0] = 0
array[1] = 1


def fibo(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    if(array[n] > 0):
        return array[n]
    else:
        array[n] = fibo(n-1)+fibo(n-2)
        return array[n]


n = int(input())
print(fibo(n))
