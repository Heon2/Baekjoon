from math import *

while(True):
    array = list(map(int, input().split()))

    if(array[0] == 0 and array[1] == 0 and array[2] == 0):
        break

    array.sort()  # 작은 순으로 정렬

    if(array[2] == sqrt(array[0]**2+array[1]**2)):
        print('right')
    else:
        print('wrong')
