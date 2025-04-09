PI: float = 3.14
RAD: int = 180

def arctan (x: float):
    precision: float = 0.0001
    k: int = 3
    signal: int = -1
    sum: float = x
    
    while x**k / k >= precision:
        sum += signal * x**k / k
        k += 2
        signal *= -1
    
    return sum

def get_angle (x: float, y: float) -> float:
    if x < 0 or y < 0:
        print('Invalid')
        return -1
    
    radians: float = 0
    
    if y < x:
        radians = arctan(y / x)
    else:
        radians = (PI / 2) - arctan(x / y)
    
    angle: float = radians * RAD / PI
    
    return angle

number_n: int = int(input('Quantia de coordenadas na lista: '))

def find_lowest_angle (n: int) -> list[float]:
    if n < 1:
        return
    
    coords: list[str] = [input(f'Digite a coordenada {i + 1}ª: ').split(', ') for i in range(n)]
    
    min_angle: float = 360
    lowest_angle: str = ''
    
    for coord in coords:
        x: float = float(coord[0])
        y: float = float(coord[1])
        
        if get_angle(x, y) < min_angle:
            min_angle = get_angle(x, y)
            lowest_angle = f'({x}, {y})'
    
    print(f'{lowest_angle} = {min_angle:.2f}°')
    return lowest_angle        

find_lowest_angle(number_n)