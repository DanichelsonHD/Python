import math as m
number: int = int(input('Digite um número inteiro com quatro dígitos: '))

def verify_conditions (n: int):
    # Verifica se somar os dois primeiros digitos com os dois segundos totalizam na raiz quadrada do número
    # Exemplo 9801 -> 98 + 01 = 99 -> 99² = 9801
    
    numbers_list: list[int] = [int(digit) for digit in str(n)]
    
    if len(numbers_list) != 4:
        print('Número não possui quatro dígitos')
        
    f2n: int = int(str(numbers_list[0]) + str(numbers_list[1]))
    s2n: int = int(str(numbers_list[2]) + str(numbers_list[3]))
    sqrt: int = int(m.sqrt(n))
    
    if (f2n + s2n) ** 2 == n:
        print('{:02d} + {:02d} = {:02d}'.format(f2n, s2n, sqrt))
    else:
        print('{:02d} + {:02d} =/= {:02d}'.format(f2n, s2n, sqrt))

verify_conditions(number)