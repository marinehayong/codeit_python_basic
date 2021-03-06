# fastcampus02-1
# 람다함수

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 람다 함수
"""
람다함수: 익명함수, 이름이 없는 함수, 1회용 함수

일반적으로 함수는 재사용성을 염두하고 작성을 한다.
똑같은, 혹은 비슷한 내용이 반복되는 코드들이 나타난다면 이때 함수가 필요하다.
재사용이 가능하기 때문에 컴퓨터 어딘가(메모리)에 존재하게 된다.
하지만 코드를 작성하다보면 예외적인 상황이 발생한다.

가정 1: 한번만 실행되면 되는 경우
한번만 실행되면 되는 경우 굳이 메모리에 적재해둬야 할 필요가?

가정 2: 간단한 연산을 할 때
def awesum(a, b):
    return a + b

lambda a, b:a + b

람다함수는 계산식 형태로 되어 있다고 해서 람다 표현식(lambda expression) 이라고 부른다.
주로 다른 함수들의 인수를 넘겨줄 때 많이 사용한다.

파이썬은 모든 것이 객체(object)로 관리된다.
파이썬 내부적으로 객체를 호출할 때 파이썬은 객체들을 호출한 값을 카운트 한다.
이때, 카운트가 0이 된다면 누구도 참조하지도 사용하지도 않고 있다고 판단하며 메모리를 환원한다.

람다로 작성된 표현식은 한번 호출되고 그 다움줄로 넘어가게 되면 누구도 참조하지 않게되어
더이상 메모리에서 관리하게 되지 않는다. -> 메모리 관리에 효율적이라는 소리

람다를 왜쓰는지 정의하자면:
메모리를 효율적으로 관리하고 싶을 때
한번만 실행하면 될 때
멋있게 쓰고 싶을 때

어떻게 쓰나요?
lambda 인자1, 인자2, 인자3..:표현식(리턴값)
*보통 한줄로 정의할 수 있는 내용들을 람다식으로 작성한다.

주의점: 람다 표현식을 사용할 땐, 간단한 연산이나 복잡하지 않은 함수들을 작성할 때 사용하라
또한, 람다 표현식 안에서는 새로운 변수를 선언할 수 없으니 새로운 변수를 선언할 필요가 있는
경우에는 def로 함수를 작성하라

람다는 map, filter, reduce, sort 등의 함수와 결합하여 사용하면 엄청난 이점을 가진다.
메모리, 가독성 면에서

map함수: 파이썬의 내장함수이며 함수와 iterable한 객체를 인자로 받는다.
iterable한 데이터를 인자로 받아 각각의 요소(item)를 전달받은 함수의 인자로 전달하여
결과를 전달하는 함수

리스트의 요소를 전부 *2를 해주고 싶다! for문을 돌려서 곱해줄 수도 있지만
map과 lambda를 사용하면 다음처럼 작성 가능
"""

some_list = [1, 2, 3, 4, 5]
result = list(map(lambda x:x*2, some_list))
print(result)

"""
*map함수는 게으른 연산을 진행하기 때문에 결과값을 사용하려면
iterable한 타입으로 변환시켜줘야 한다.
"""

# list, tuple, dictionary, set 강의랑 들은 강의 한번 더 들어보기
