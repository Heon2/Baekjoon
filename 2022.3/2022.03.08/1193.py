from math import *
x = int(input())  # 5


n = ceil((-1+sqrt(1+8*x))/2)  # 3
if(n % 2 == 0):
    # 분자
    a = x - ((n-1)*(n))//2
    # 분모
    b = (n+1)-(x-((n*(n-1))//2))
else:
    # 분자
    a = (n+1)-(x-((n*(n-1))//2))
    # 분모
    b = x - ((n-1)*(n))//2

print(a, '/', b, sep='')
