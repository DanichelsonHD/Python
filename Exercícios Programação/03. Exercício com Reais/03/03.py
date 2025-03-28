number: int = int(input('Digite uma quantia: '))

def verify_coords (n: int):
    for _ in range(n):
        x, y = map(float, input('Digite as coordenadas separadas por um espaço: ').split())
        
        if x > -1 and y > -1:
            if x**2 + y**2 < 2:
                print('Pertence a H')
                continue
        
        print('Não pertence a H')

verify_coords(number)