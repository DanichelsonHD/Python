number: int = int(input('Digite um número inteiro: '))

def perfect_number (n: int):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return 'É um número perfeito' if sum == n else 'Não é um número perfeito'

print(perfect_number(number))