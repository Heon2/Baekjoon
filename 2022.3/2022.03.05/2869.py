from math import *

A, B, V = map(int, input().split())
result = 0

result = ceil((V-A)/(A-B))+1

print(result)
