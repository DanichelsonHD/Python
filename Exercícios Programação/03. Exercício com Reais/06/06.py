import math as m

number_x: int = int(input('Digite um número pra calcular o Cosseno: '))
number_n: int = int(input('Digite um número pra Série Taylor: '))

def calc_cos (x: int, n: int):
    cos: float = 1.0
    signal: int = -1
    i: int = 2
    
    while i < 2*n:
        cos += signal * (x**i / m.factorial(i))
        signal *= -1
        i += 2
        
    print(f'Aproximação do cosseno de {x} com o k de {n} é: {cos:.10f}')

calc_cos(number_x, number_n)