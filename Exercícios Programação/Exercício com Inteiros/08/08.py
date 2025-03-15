import math as m

n: int = int(input('Digite um número inteiro: '))

def calc_factorial_ (number: int):
    match number:
        case 0:
            return 1
        case _ if number < 0:
            return 'Número inválido'
        case _:
            return number * calc_factorial(number - 1)

def calc_factorial (number: int):
    return m.factorial(number)

print(calc_factorial_(n))