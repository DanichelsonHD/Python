number_m: int = int(input('Digite um número para o maior X possível: '))
number_n: int = int(input('Digite um número para o maior Y possível: '))

def find_max_equation (n: int, m: int):
    max_value: int = 0
    max_x: int = 0
    max_y: int = 0
    
    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if equation(x, y) > max_value:
                max_value = equation(x, y)
                max_x = x
                max_y = y
    
    print('\nMaior valor {}\nX do maior valor {}\nY do maior valor {}'.format(max_value, max_x, max_y))
    return(max_value)

def equation (x: int, y: int) -> int:
    return (x*y - x**2 + y)

find_max_equation(number_n, number_m)