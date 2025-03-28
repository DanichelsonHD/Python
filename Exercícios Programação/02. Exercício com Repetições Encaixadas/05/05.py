number_m: int = int(input('Digite um número: '))

def consecutive_numbers (m: int):
    for n in range(1, m + 1):
        odd: list[int] = get_odd_numbers(n)
        print(f'O número {n}³ = {n**3} é a soma de {odd}')

def get_odd_numbers (n: int) -> list[int]:
    odd_numbers: list[int] = []
    average: int = n**3 // n
    
    for i in range(average - n, average + n + 1):
        if i % 2 == 1 and len(odd_numbers) < n:
            odd_numbers.append(i)
    
    return odd_numbers

consecutive_numbers(number_m)