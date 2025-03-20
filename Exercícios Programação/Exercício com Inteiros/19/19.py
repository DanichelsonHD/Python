number_1: int = int(input('Digite um número inteiro: '))
number_2: int = int(input('Digite outro número inteiro: '))
number_3: int = int(input('Digite mais um número inteiro: '))

def put_in_order (n1: int, n2: int, n3: int) -> list[int]:
    new_order = [n1, n2, n3]
    new_order.sort()
    print(new_order)
    return new_order

put_in_order(number_1, number_2, number_3)