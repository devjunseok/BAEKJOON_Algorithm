from random import randint
from datetime import datetime
import time



print("게임의 자리수를 설정합니다")
n = int(input()) #자리수 설정


# 랜덤하게 입력되는 3자리수
numbers = []
print("0과 9 사이의 서로 다른 숫자를 설정한 자리수 만큼 랜덤한 순서로 뽑았습니다.")
while len(numbers) < n:
    new_numbers = randint(0,9)
    if new_numbers in numbers:
        new_numbers = randint(0, 9)
    numbers.append(new_numbers)
    print(numbers)

# 사용자가 값을 정확하게 맞출때까지 무한반복
start = time.time()
count = 0
while True:

    # 사용자가 입력하는 3자리수
   
    user = []
    print("숫자를 하나씩 차례대로 입력하세요. (종료 - exit)")
    while len(user) < n:
        # try:
            user_input = input()
            if user_input == "exit":
                print("프로그램을 종료합니다")
                quit()
    
            user_numbers = int(user_input)
               
            if user_numbers in user:
                print("중복되는 수 입니다. 다시 입력해주세요.")
            elif user_numbers > 9:
                print("범위를 벗어나는 수입니다.다시 입력해주세요.")
            user.append(user_numbers)
            print(user)
              
    i = 0
    s = 0
    b = 0
    o = 0
    while i < len(numbers):
        if numbers[i] == user[i]:
            s = s + 1
        elif user[i] in numbers:
            b = b + 1
        else:
            o = o + 1
        i += 1
    print("%d Strike %d Ball %d Out \n" % (s, b, o))
    count += 1
    if s == n:
        print("축하합니다. %d번만에 세 숫자의 갑과 위치를 모두 맞추셨습니다." % count)
        break
end = time.time()

print(f"게임 시작 후 걸린 시간: {end-start:.2f} 초")
print( f"게임 종료 시간: {datetime.now()}")