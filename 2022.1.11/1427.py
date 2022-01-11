num = input()
my_list = []

for i in num:
    my_list.append(i)

my_list.sort(reverse=True)
print(('').join(my_list))
