n = input()
number = n  # 26
if(int(n) < 10):
    n = '0'+n
count = 0


while(True):
    count += 1
    if(int(number) < 10):
        number = '0'+str(int(number))
    a = number[0]  # 2
    b = number[1]  # 6
    sum = str(int(a) + int(b))  # 8
    a = b  # 2 --> 6
    b = sum[-1]  # 6 --> 8
    number = a + b  # 68
    if(number == n):
        break

print(count)
