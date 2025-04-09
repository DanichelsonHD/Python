number_n: int = int(input('Quantia de números na lista: '))

def verify_n (n: int) -> int:
    if n < 1:
        return
    
    n_list: list[int] = [int(input(f'Digite o {i + 1} número: ')) for i in range(n)]
    
    odd: int = 0
    even: int = 0
    
    for number in n_list:
        if number % 2 == 0:
            even += 1
        elif number % 2 == 1: 
            odd += 1
    
    verify_pyramidal(n, n_list)
    
    if even != 0 and odd == 0:
        print('Números pares')
        return 0
    elif odd != 0 and even == 0:
        print('Números ímpares')
        return 1
    
    print('Números misturados')
    return -1

def verify_pyramidal (n: int, n_list: list[int]):
    m: int = 0
    while n != 0:
        m += 1
        n -= m
        
        if n < 0:
            print('Não é piramidal')
            return False
    
    print(f'É piramidal {m}-alternante')
    return True

verify_n(number_n)