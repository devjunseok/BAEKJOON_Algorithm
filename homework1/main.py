from func import add_func, subtract_func, multiply_func, divide_func

print("연산하고 싶은 숫자를 한 줄에 한개씩 총 두 줄, 마지막줄엔 연산자(+,-,*,/) 입력해주세요")

num1 = int(input())
num2 = int(input())
operator = input()


if operator == '+':
     add_func(num1,num2)
elif operator == '-':
    subtract_func(num1,num2)
elif operator == '*':
    multiply_func(num1,num2)
elif operator == '/':
    divide_func(num1,num2)
else:
    print('잘못 입력하셨습니다')


