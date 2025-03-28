number: int = int(input('Digite um número: '))

def get_factor_numbers (n: int):
    n_copy: int = n
    multiples_list: list[int] = []
    
    for i in range(2, n_copy):
        if n_copy > 0 and n_copy % i == 0 and is_prime(i):
            divide_by(n_copy, i, multiples_list)
            
            
    print(f'\nO número {n} pode ser divido nos fatores primos: {show_multiples(multiples_list)}')
    
def is_prime (i: int) -> bool:
    counter: int = 0
    
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    
    if counter == 2:
        return True
    
    return False

def divide_by (n: int, i: int, multiples_list: list[int]):
    while n % i == 0:
        n = n / i
        multiples_list.append(i)
    
    return multiples_list, n

def show_multiples (multiples_list) -> str:
    new_list: list[str] = []
    multiplicity: int = 0
    last_number: int = 0
    
    for i in multiples_list:
        if last_number != i:
            new_list.append(f'{i}x{multiples_list.count(i)}')
            last_number = i
    
    
    
    return ', '.join(j for j in new_list)

get_factor_numbers(number)