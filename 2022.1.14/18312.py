num, k = map(int, input().split())
count = 0
for hour in range(num+1):
    if(hour < 10):
        hour = '0'+str(hour)
    for min in range(60):
        if(min < 10):
            min = '0' + str(min)
        for sec in range(60):
            if(sec < 10):
                sec = '0' + str(sec)
            if str(k) in str(hour)+str(min)+str(sec):
                count += 1

print(count)
