number_a: str = input('Digite um número com vários algarismos: ')
number_b: str = input('Digite outro número com menos algarismos: ')

def verify_b_in_a (a: str, b: str):
    for i in range(len(b)):
        for j in range(0, len(b)):
            if i == j:
                val: int = len(a) - len(b) + j
                print(f'{a[val]}, {b[i]}\n{j}, {i}')
                
                if int(a[val]) != int(b[i]):
                    print('Não encaixa')
                    return False
    
    print('Encaixa')
    return True

def verify_minor_in_major (a: str, b: str):
    temp = 0
    if len(a) < len(b):
        temp = a
        a = b
        b = temp
    
    for i in range(len(b)):
        valA: int = len(a) - i - 1
        valB: int = len(b) - i - 1
        print(f'{a[valA]}, {b[valB]}')
        
        if int(a[valA]) != int(b[valB]):
            print('Não encaixa')
            return False
    
    if temp == 0:
        print('B encaixa em A')
        return True
    
    print('A encaixa em B')
    return True

verify_minor_in_major(number_a, number_b)