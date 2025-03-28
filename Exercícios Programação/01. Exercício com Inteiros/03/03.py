n: int = int(input("Digite um número: "))

def calc_odd_numbers__ (n: int):
    total_numbers: int = 0
    number_counter: int = 1
    while total_numbers < n:
        if number_counter % 2 == 0:
            number_counter += 1
        else:
            print(number_counter)
            total_numbers += 1
            number_counter += 1

def calc_odd_numbers (n: int):
    total_numbers: int = 0
    number_counter: int = 1
    while total_numbers < n:
        print(number_counter)
        total_numbers += 1
        number_counter += 2

calc_odd_numbers(n)
