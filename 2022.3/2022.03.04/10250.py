T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if((N % H) == 0):
        a = str((N//H))
        b = str(H)
    else:
        a = str((N//H)+1)
        b = str((N % H))
    if(int(a) < 10):
        a = '0' + a
    result = int(b+a)
    print(result)
