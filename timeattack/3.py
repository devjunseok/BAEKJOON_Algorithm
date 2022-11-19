def get_even_numbers(numbers, numbers2):
    for i in range(numbers, numbers2):  # [1,2,3,4,...,100]
        if i%2 == 0:
           print(i)

def get_some_numbers(numbers, numbers2):
    for i in range(numbers, numbers2):  # [1,2,3,4,...,100]
        if i % 3 == 0 and i % 15 != 0:
           print(i)
        i += 1

def main():
    numbers = 1
    numbers2 = 10000
    even_numbers = get_even_numbers(numbers, numbers2)
    some_numbers = get_some_numbers(numbers, numbers2)

   
    
main() 