n = int(input())  # 약수의 갯수
array = list(map(int, input().split()))

print(max(array)*min(array))
