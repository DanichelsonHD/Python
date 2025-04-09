def f1 (x: int, y: int) -> float:
    res: float = 0
    
    if x == 0 and y == 0:
        return res
    
    if y != 0:
        res = x / y
    else:
        res = 1 / x
    
    while x > y:
        res += x / y
        x -= 1
    
    return res

def main():
    try:
        a, b = map(int, input('Digite 2 números separados por espaço: ').split())
        c, d = map(float, input('Digite outros 2 números separados por espaço: ').split())
    except ValueError:
        print('Erro')
        exit()
    
    while a < b:
        if c > d:
            d = f1(b, a)
            b -= 1
        else:
            c = 1 / f1(a, b)
            a += 1
        
        print(f'a = {a}, b = {b}, c = {c:.2f}, d = {d:.2f}')

main()