number_1: int = int(input('Digite o primeiro número: '))
number_2: int = int(input('Digite o segundo número: '))

def euclids_algorithm (n1: int, n2: int) -> int:
    if n1 % n2 != 0:
        return euclids_algorithm(n2, n1 % n2)
    print("O MDC é: %d" % n2)
    return n2

euclids_algorithm(number_1, number_2)