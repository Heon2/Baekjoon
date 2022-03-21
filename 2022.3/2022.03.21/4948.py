# nums = 2와 홀수로 이루어진 집합
nums = {x for x in range(2, 246913) if x == 2 or x % 2 == 1}

# odd_num 3부터 246912 제곱근+1 까지의 홀수 집합
for odd_num in range(3, int(246912**0.5) + 1, 2):
    nums -= {i for i in range(2 * odd_num, 246_913, odd_num) if i in nums}

while True:
    n = int(input())
    if n == 0:
        break

    # nums 집합에서 n보다 크고 2*n보다 작거나 같은 수의 리스트
    prime_number = [i for i in range(n+1, 2*n+1) if i in nums]
    print(len(prime_number))
