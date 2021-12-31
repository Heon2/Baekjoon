num1 = set(range(1, 10001))
num2 = set()

def d(n):   # n과 n의 각 자리수를 더해서 리턴
    str_n = str(n)
    answer = n
    for i in str_n:
        answer += int(i)

    return answer

for i in range(1,10001):
    num2.add(d(i))

self_num = sorted(num1 - num2)  # 리스트의 형태로 정렬후 저징

for i in self_num:
    print(i)
