import operator
my_dict = {}

string = input().upper()

for i in string:  #모든 알파벳을 my_dict에 등록
    my_dict[i] = 0

for i in string:  #key값이 같으면 value 1증가
    my_dict[i] = my_dict[i] + 1

my_list = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)   #딕셔너리를 리스트의 형태로 value값으로 정렬(내림차순)

if(len(my_list)==1):  #입력한 문자열의 길이가 1개일때
    print(my_list[0][0])
elif(my_list[0][1]!=my_list[1][1]):  #가장 많이 사용된 알파벳이 하나일때 
    print(my_list[0][0])
else:                           #가장 많이 사용된 알파벳이 두개 이상일때
    print('?')


##################################### 깔끔한 다른 풀이
#word = input().lower()      # word = mississipi / baaa
#word_list = list(set(word)) # word_list = ['m', 'i', 's', 'p'] / ['b', 'a']
#cnt = []

#for i in word_list:         # i = m, i, s, p / b, a
#    count = word.count(i)
#    cnt.append(count)       # cnt = [4, 4, 1, 1] / [1, 3]
#
#if cnt.count(max(cnt)) >= 2:
#    print("?")
#else:
#    print(word_list[(cnt.index(max(cnt)))].upper())