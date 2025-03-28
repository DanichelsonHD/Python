n: int = int(input('Digite um número: '))

def sum_even_numbers (n: int):
    sum = 0
    even_number = 2
    for i in range(n):
        sum += even_number
        even_number += 2
    return sum

print(sum_even_numbers(n))
    