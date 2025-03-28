number: int = int(input('Digite uma quantia: '))

def verify_h (n: int):
    count: int = 0
    for _ in range(n):
        x, y = map(float, input('Digite as coordenadas separadas por um espaço: ').split())
        if h1(x, y) or h2(x, y):
            print(f'{x} e {y} pertencem ao conjunto H')
            count += 1
        else:
            print(f'{x} e {y} não pertencem ao conjunto H')
    print('Total de pontos q pertencem ao conjunto H:', count)
        
def h1 (x: int, y: int) -> bool:
    if x < 1 and y < 1:
        if y + x**2 + 2*x - 3 < 1:
            return True
    return False

def h2 (x: int, y: int) -> bool:
    if x > -1 and y + x**2 - 2*x - 3 < 1:
        return True
    return False

verify_h(number)