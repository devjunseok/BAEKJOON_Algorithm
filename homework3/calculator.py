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

a, b = map(float, input("두 개의 숫자를 입력하세요. : ").split())
calc = Calculator(a, b)
calculate = input("계산 방식을 입력하세요. ex): +, -, *, / : ")

if calculate == "+":
    print(calc.plus())
elif calculate == "-":
    print(calc.minus())
elif calculate == "*":
    print(calc.multiple())
elif calculate == "/":
    print(calc.divide())