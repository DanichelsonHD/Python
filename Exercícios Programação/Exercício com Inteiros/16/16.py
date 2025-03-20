binary: str = input('Digite um número binário: ')

def binary_to_decimal (b: str):
    sum: int = 0
    for j, i in enumerate(b):
        index = len(b) - (j + 1)
        if i != '0' and i != '1':
            print('Não é binário')
            return
        if i == '0':
            pass
        if i == '1':
            sum += 2**index
    print(str(sum))

binary_to_decimal(binary)