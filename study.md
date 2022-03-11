# 리스트의 메소드

- **append** - 리스트가 포함된 데이터에서 특정 데이터를 추가하고 싶을 때 append 메소드를 사용합니다.

- **insert** - insert() 메소드는 리스트의 index 번째 위치에 인수로 지정한 데이터를 삽입합니다.

- **sort** - sort() 메소드는 리스트에 저장된 데이터를 오름차순으로 정렬합니다.

- **sort(reverse = True)** - sort() 메소드에 reverse = True 옵션을 지정하면 내림 차순으로 정렬됩니다.

- **reverse** - reverse() 메소드는 리스트에 저장된 데이터의 순서를 반대로 출력합니다.

- **index** - index() 메소드는 인수로 지정된 데이터가 리스트에 저장되어있을 경우 첫 번째 데이터의 위치를 얻어옵니다.

  index() 메소드의 실행 결과가 0 이상이라면 지정된 데이터가 리스트에 포함되어 있다는 의미로 사용할 수 있으며, 포함되어 있지 않을 경우 에러가 발생합니다.

- **count** - count() 메소드는 인수로 지정된 데이터가 리스트에 포함되어 있는 개수를 얻어옵니다.

  count() 메소드의 **실행 결과가 1 이상**이면 인수로 지정된 데이터가 **리스트에 포함되어 있다는 의미**로 사용할 수 있으며, **실행 결과가 2 이상**이면 인수로 지정된 데이터가 **중복되서 리스트에 포함되어 있다는 의미**로 사용할 수 있으며, **실행 결과가 0 이면** 인수로 지정된 **데이터가 없다는 의미**로 사용할 수 있다.

- **remove** - remove() 메소드는 인수로 지정된 데이터를 리스트에서 제거합니다. (첫 번째 데이터만 제거)

- **pop** - pop() 메소드는 리스트에 저장된 **마지막 데이터를 얻어온 후 제거**하고 pop() 메소드의 인수로 **인덱스를 지정하면 지정된 인덱스 위치의 데이터를 얻어온 후 제거**합니다.

- **extend** - extend() 메소드는 리스트를 확장합니다. ( '+' 연산이 실행)  ex. a.extend([4, 5])



# 집합 (set)

### 집합의 특징

\- **집합**은 리스트와 비슷하지만, **원소들 사이에 순서가 없고, 원소의 중복을 허용하지 않는다**는 면에서 리스트와는 다르다.

\- **집합**은 **원소들 사이에 순서가 없다.**

\- **집합**은 **원소의 중복을 허용하지 않는다.**

\- 집합은 **원소들이 어떤 "위치"를 가지지도 않고**, 일렬로 나열한다는 의미도 적용할 수 없으므로, **선형 자료구조로 볼 수 없다.**



**set 선언방법**

S = {elem0, elem1, elem2, ... , elem(n-1)}﻿



**파이썬의 set는 [ ](대괄호)로 특정 요소만 출력할 수 없다.**

fruits = {'apple', 'strawberry', 'cranberry', 'banana', 'grape', 'peach'} 

print(fruits[1])   ## 에러

| **연산**                                                     | **집합 연산**  | **메서드**                             |
| ------------------------------------------------------------ | -------------- | -------------------------------------- |
| 합집합(union)(OR)                                            | 세트1 \| 세트2 | set.union(세트1, 세트2)                |
| 교집합(intersection)(AND)                                    | 세트1 & 세트2  | set.intersection(세트1, 세트2)         |
| 차집합(difference)                                           | 세트1 - 세트2  | set.difference(세트1, 세트2)           |
| 대칭차집합(symmetric difference)(XOR)서로 다르면 참두 집합 중 겹치지 않는 요소만 포함 | 세트1 ^ 세트2  | set.symmetric_difference(세트1, 세트2) |



| **연산**                              | **집합 연산 후 할당 연산자 사용하기** | **메서드**                               |
| ------------------------------------- | ------------------------------------- | ---------------------------------------- |
| 합집합(union)(OR)                     | 세트1 \|= 세트2                       | 세트1.update(세트2)                      |
| 교집합(intersection)(AND)             | 세트1 &= 세트2                        | 세트1.intersection_update(세트2)         |
| 차집합(difference)                    | 세트1 -= 세트2                        | 세트1.difference_update(세트2)           |
| 대칭차집합(symmetric difference)(XOR) | 세트1 ^= 세트2                        | 세트1.symmetric_difference_update(세트2) |

**EX. 집합 객체를 만들고, 합집합, 교집합, 차집합 등의 연산을 처리하는 파이썬 코드**

```
s1 = {1, 2, 3}                # 집합 객체
s2 = {2, 3, 4, 5}             # 집합 객체
s3 = s1.union(s2)             # 합집합
s4 = s1.intersection(s2)      # 교집합
s5 = s1 - s2 #차집합
print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)
print("s5:", s5)


s1: {1, 2, 3}                
s2: {2, 3, 4, 5}           
s3: {1, 2, 3, 4, 5}
s4: {2, 3}
s5: {1}
```





| **set 조작 메서드** | **설명**                                                     |
| ------------------- | ------------------------------------------------------------ |
| 세트.add(요소)      | * 세트에 요소를 추가한다.                                    |
| 세트.remove(요소)   | * 세트에서 특정 요소를 삭제한다.* 요소가 없으면, 에러를 발생시킨다. |
| 세트.discard(요소)  | * 세트에서 특정 요소를 삭제한다.* 요소가 없으면, 그냥 넘어간다. |
| 세트.pop()          | * 세트에서 임의의 요소를 삭제하고, 해당 요소를 반환한다.* 만약 요소가 없으면, 에러를 발생시킨다. |
| 세트.clear()        | * 세트에서 모든 요소를 삭제한다.                             |
| len(세트)           | * 세트의 요소 개수(길이)를 구한다.                           |

#### ***list = sorted(세트)의 형태로 리스트형에 정렬하여 저장할수 있다.



### set은 set 안에 set을 중첩해서 넣을 수 없다.



frozenset : 내용을 변경할 수 없는 세트

\>> 집합 연산, 메서드에서 요소를 추가하거나 삭제하는 연산, 메서드는 사용할 수 없다.

\>> frozenset 안에 frozenset을 중첩해서 넣을 수 있으므로, 세트 안에 세트를 넣고 싶을 때 사용



# 빠른 입력받는법

```
import sys
input = sys.stdin.readline
```

이 코드르 추가해준다





# itertools 라이브러리

**itertools**는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하는 라이브러리이다

클래스는 크게 permutations, combinations 를 주로 사용한다.



# permutations

**permutation**는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.

permutations 는 클래스이기 때문에 객체 초기화 이후 리스트 자료형으로 반환하여 사용한다

```
from itertools import permutations

a = ['a','b','c']
x = list(permutations(a,2))
print(x)
```

지정한 리스트 a 에서 두개를 뽑아 나올수 있는 경우의 수를 출력해준다

결과 [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

이때 permutations(ar,n) 안에서 n은 len(ar)을 초과 할수 없다



# combinations

**combinations**는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.

combinations 또한 클래스이기에 객체 초기화 이후에는 리스트 자료형으로 변환한뒤 사용한다

```
from itertools import combinations

a = ['a','b','c']
x = list(combinations(a,2))
print(x)
```

permutations와의 큰 차이점이라면 순서를 생각하지 않기에 a,b = b,a 취급을 한다

결과는 [('a', 'b'), ('a', 'c'), ('b', 'c')]

위와 대조해보면 permutations 의 경우 6개인 반면 combinations 는 3개임을 알 수 있다



# product

**product**는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산한다 하지만 원소를 중복하여 뽑는다.

product 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.

product 또한 클래스이기에 list로 반환하여 사용한다

```
from itertools import product

a = ['a','b','c']
x = list(product(a,repeat=2))
print(x)
```

결과는 [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]

중복을 허용하기에 permutations 와 combinations 를 비교했을 때에 비해 9개라는 결과가 나오는 것을 알 수 있다



# combinations_with_replacement

**combinations_with_replacement**는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다. 하지만 원소를 중복하여 뽑는다

combinations_with_replacement 또한 클래스이기에 리스트로 변환하여 사용한다

```
from itertools import combinations_with_replacement

a = ['a','b','c']
x = list(combinations_with_replacement(a,2))
print(x)
```

결과는 [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]



---

| 구분 | permutations | combinations | combinations_with_replacement | product |
| ---- | ------------ | ------------ | ----------------------------- | ------- |
| 순서 | O            | X            | X                             | O       |
| 중복 | X            | X            | O                             | O       |

종합으로 생각했을 때 경우의 수가 가장 많은 것부터 작은 순으로 나열한다면

product > combinations_with_replacement > permutations > combinations

이며 itertools는 경우의 수를 셈으로서 수학의 확률 문제에 쓰임이 많을 것 같다

