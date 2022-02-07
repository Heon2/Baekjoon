N = input()
nums = set()

def solve(N):
    if(int(N)<100):  #100보다 작은 자연수는 무조건 한수
        nums.add(N)
        return 0

    gap = int(N[1])-int(N[0])  #기준으로 잡을 차이
    for i in range(1,len(N)-1):
        if(gap != int(N[i+1])-int(N[i])):  #차이가 다르면 add없이 break
            return 0
    nums.add(N)

for i in range(1,int(N)+1):
    solve(str(i))

print(len(nums))