s = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in lst:
    while i in s:
        cnt += s.count(i)
        s = s.replace(i, '0'*len(i))
print(cnt + len(s) - s.count('0'))
