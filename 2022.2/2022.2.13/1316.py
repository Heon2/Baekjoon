t = int(input())     # 테스트 캐이스의 숫자를 받아준다. (총 받을 문자열 수)
cnt = 0              # 그룹 단어가 아닌 문자열을 세기 위한 변수

for i in range(t):          # 테스트 개수만큼 도는 반복문
    str = input()           # 문자열을 받는다.
    for i in range(len(str)):       # 문자열요소의 개수만큼 반복문을 반복(요소마다 검사를 위해)
        str = str.replace(str[0], str[0].upper())  # 문자열의 첫 문자와 같은 문자를 대문자로!
        str = str.lstrip(str[0].upper())       # 문자열 왼쪽편에 첫 문자와 같은 대문자면 지운다.
        if str == "":               # 다 지워져서 빈 문자열이면 그룹단어이기에 탈출
            break
        if str.islower():           # 대문자를 지운후 문자열이 소문자면 1차 통과 다음 문자 검사
            continue
        else:                       # 왼쪽 대문자를 지웠는데도 대문자가 있으면 떨어졌는 문자가
            cnt += 1                # 있었단 소리 따라서 그룹문자 아니니깐 +1 증가
            break                   # 더 볼 필요없이 탈출

print(t - cnt)                      # 총 받은 문자열 - 그룹문자 아닌 것 = 그룹문자
