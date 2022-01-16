num = int(input())

array = []
for i in range(num):
    # ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
    array.append(input())

set_array = list(set(array))    # 중복된 단어 제거
sorted_array = []
for i in set_array:
    # ex)[(3,'but'),(1,'i'),(4,'wont')]
    sorted_array.append((len(i), i))

result = sorted(sorted_array)  # [(1,'i'),(3,'but'),(4,'wont')]

for len, i in result:
    print(i)
