number: int = int(input('Digite um número inteiro: '))

def calc_fibonacci (n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calc_fibonacci(n - 1) + calc_fibonacci(n - 2)