number_1: int = int(input('Digite um número inteiro: '))
number_2: int = int(input('Digite outro número inteiro: '))
number_3: int = int(input('Digite mais um número inteiro: '))

def verify_if_triangular (n1: int, n2: int, n3: int) -> bool:
    if n1**2 == n2**2 + n3**2 or n2**2 == n1**2 + n3**2 or n3**2 == n1**2 + n2**2:
        print('É um triangulo retângulo')
        return True
    else:
        print('Não é um triangulo retângulo')
        return False
    
verify_if_triangular(number_1, number_2, number_3)