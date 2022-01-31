N, K = map(int, input().split())
array = []
result = 0
for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)

for i in array:
    if(K == 0):
        break
    result += K//i
    K = K % i

print(result)
