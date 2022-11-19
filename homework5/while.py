
def int_value(number):
    sum = number * 2
    return sum



count = 0
while True:
    user_input = input("값을 입력하세요:")
    if count == 5:
        break
    elif user_input == "exit":
        print("프로그램을 종료합니다")
        quit()
    elif user_input.isdigit():
        sum = int(user_input) * 2
        print(sum)
        count += 1
    else:
        print(f"입력한 문자값은 {user_input}입니다.")
        
