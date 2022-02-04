import sys
imput = sys.stdin.readline

n = int(input())  # 도시의 개수, 4
road = list(map(int, input().split()))  # 도로, [2,3,1]
pay = list(map(int, input().split()))  # 기름가격, [5,2,4,1]

min = pay[0]
result = min*road[0]  # 총 가격

for i in range(1, n-1):
    if(min < pay[i]):
        result += min*road[i]
    else:
        min = pay[i]
        result += min*road[i]

print(result)
