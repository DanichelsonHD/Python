import math as m

number_x: float = float(input('Digite um número pra calcular o Seno: '))
number_n: float = float(input('Digite um número pra limitar a Série Taylor: '))

def calc_sin (x: float, n: float):
    sin: float = x
    signal: int = -1
    k: int = 1
    t: float = x
    
    while t >= n:
        kp: int = 2 * k + 1
        t = x**kp / m.factorial(kp)
        sin += signal * t
        signal *= -1
        k += 1
        
    
    print(f'Aproximação do seno de {x} com o k de {n} é: {sin:.10f}')
        
calc_sin(number_x, number_n)