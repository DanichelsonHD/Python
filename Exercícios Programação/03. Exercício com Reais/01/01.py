capital: int = int(input('Digite um valor para o capital: '))
fees: float = float(input('Digite um  valor de juros: '))

def calc_anual_fees (c: int, f: float):
    for i in range(12):
        c += c * (f/100)

    print(f'{c:.2f}')
    return c

calc_anual_fees(capital, fees)