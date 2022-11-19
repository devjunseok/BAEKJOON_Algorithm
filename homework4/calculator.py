class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def plus(self):
        result = self.first + self.second
        return result

    def minus(self):
        result = self.first - self.second
        return result

    def multiple(self):
        result = self.first * self.second
        return result

    def divide(self):
        result = self.first / self.second
        return result
try:
    a, b = map(float, input("두 개의 숫자를 입력하세요. : ").split())
    calc = Calculator(a, b)
except:
    print("잘못된 입력값 입니다.")
calculate = input("계산 방식을 입력하세요. ex): +, -, *, / : ")
try:
    if calculate == "+":
        print(calc.plus())
    elif calculate == "-":
        print(calc.minus())
    elif calculate == "*":
        print(calc.multiple())
    elif calculate == "/":
         print(calc.divide())
except ZeroDivisionError: # 0으로 나누면서 에러가 발생했을 때
    print("0으로는 나눌수 없습니다.")
except: # 위에서 정의하지 않은 에러가 발생했을 때(권장하지 않음)
    print("부등호만 입력 가능합니다")