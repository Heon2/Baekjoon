str = input().split(' ')
H = int(str[0])
M = int(str[1])

M = M - 45
if(M<0):
    H = H - 1
    M = 60+M
    if(H<0):
        H=23

print(H, M)