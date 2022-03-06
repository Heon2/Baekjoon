A, B = map(str, input().split())
array_A = list(A)
array_A.reverse()
array_B = list(B)
array_B.reverse()
result = []
x = 0  # 오버플로우 초기값

for i in range(max(len(A), len(B))):
    sum = 0 + x  # 앞에서 받아온 오버플로우
    if(i < len(A)):
        sum += int(array_A[i])
    if(i < len(B)):
        sum += int(array_B[i])
    x = sum//10  # 오버플로우
    y = sum % 10  # result에 저장할 수
    result.append(str(y))
    if(i == max(len(A), len(B))-1 and x == 1):
        result.append('1')

result.reverse()
print(''.join(result))
