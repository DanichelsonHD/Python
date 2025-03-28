number: int = int(input('Digite um número: '))

def calc_hn (n: int):
    hn: int = 0
    for k in range(1, n + 1):
        hn += 1/k
    print(hn)

calc_hn(number)