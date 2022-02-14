from re import A


n = int(input())
a = n//3
b = n//5
min = 100000
count = 0

for i in range(a+1):
    for k in range(b+1):
        if((n-3*i-5*k) == 0):
            if(min > (i+k)):
                min = i+k


if(min == 100000):
    print(-1)
else:
    print(min)
