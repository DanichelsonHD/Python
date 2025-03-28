n: int = int(input('Escolha um número para a quantia de múltiplos: '))
i: int = int(input('Escolha um número pros primeiros múltiplos: '))
j: int = int(input('Escolha um número pros outros múltiplos: '))

def calc_multiple (n: int, i: int, j: int) -> list[int]:
    multiples: list[int] = []
    counter: int = 0
    while len(multiples) < n:
        if counter % i == 0 or counter % j == 0:
            multiples.append(counter)
            print(counter)
        counter += 1

calc_multiple(n, i, j)
        