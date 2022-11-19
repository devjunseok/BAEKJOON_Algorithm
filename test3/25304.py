def calculate(value):
    return value[0] * value[1]


def receipt(X, receipt_list):
    answer = "No"
    calculate_value = sum([calculate(value) for value in receipt_list])

    if X == calculate_value:
        answer = "Yes"

    return answer


if __name__ == "__main__":
    X = int(input())

    receipt_list = []

    for _ in range(int(input())):
        money, num = map(int, input().split())

        receipt_list.append((money, num))

    print(receipt(X, receipt_list))
