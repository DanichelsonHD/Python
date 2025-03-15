big_number: int = int(input('Digite um número: '))

def separate_big_numbers_ (n: int) -> list[int]:
    return sorted([int(digit) for digit in str(n)])

def separate_big_numbers (n: int) -> list[int]:
    small_numbers: list[int] = []
    number: str = str(n)
    for i in range(len(number)):
        small_numbers.append(int(number[i]))
    
    return sorted(small_numbers)
    

print(separate_big_numbers(big_number))