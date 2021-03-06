# 남박사06-1
# 2019-12-07 08:55

# 숫자맞추기 게임(파이썬 기초, 랜덤 함수, 반복문, 조건문)

import random
import os


# msg의 의미를 잘 모르겠어요
def input_check(msg, casting=int):
    while True:
        try:
            user_input = casting(input("몇 일까요? "))
            return user_input
        except:
            continue

chance = 10
count = 0

number = random.randint(1, 99)
os.system('cls')
print("1부터 99까지의 숫자를 10번 안에 맞춰 보세요.")

while count < chance:
    count += 1
    user_input = input_check("몇 일까요? ")
    if number == user_input:
        break
    elif user_input < number:
        print("{} 보다 큰 숫자 입니다.".format(user_input))
    elif user_input > number:
        print("{} 보다 작은 숫자 입니다.".format(user_input))

if user_input == number:
    print("정답! {}이 맞습니다".format(number))
else:
    print("실패! 정답은 {}였습니다.".format(number))