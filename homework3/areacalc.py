PIE = 3.14

class Calculator:
    PIE = 3.14
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def square(self):
        result = self.first * self.second
        return result

    def triangle(self):
        result = self.first * self.second * 0.5
        return result

    def circle(self):
        result = self.first * 0.5 * 0.5 * PIE
        return result

a, b = map(float, input("가로 세로를 입력하세요. : ").split())
area = Calculator(a, b)
figure = input("도형의 종류를 입력하세요. ex) 사각형, 삼각형, 원 : ")

if figure == "사각형":
    print(area.square())
elif figure == "삼각형":
    print(area.triangle())
elif figure == "원":
    print(area.circle())
else:
    print("잘못된 입력값입니다")