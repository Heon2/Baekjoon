num = int(input())  # 5, 입력받을 갯수
my_list = []
for _ in range(num):           # 5,2,3,4,1
    a = int(input())
    my_list.append(a)

my_list.sort()

for i in my_list:
    print(i)
