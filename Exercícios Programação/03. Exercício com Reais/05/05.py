import math as m

print('Calcular fórmula 2° grau, exemplo: Ax² + Bx + C = 0')
a, b, c = map(int, input('Digite três números, para A, B e C separados por espaço: ').split())

def second_degree_formula (a: int, b: int, c: int):
    if a == 0:
        print('Impossível calcular')
        return
    
    x1 = None # -b + Vdelta / 2a
    x2 = None # -b - Vdelta / 2a
    
    delta: int = b**2 - (4 * a * c)
    imaginary: bool = False
    
    if delta < 0:
        delta *= -1
        imaginary = True
        
    if delta == 0:
        x1 = -b / (2 * a)
        
        print(f'A raíz é: {x1}') 
        return x1
    
    if imaginary:
        b2a = -b / (2 * a)
        d2a = m.sqrt(delta) / (2* a)
        
        x1 = '{:.2f} + {:.2f}i'.format(b2a, d2a)
        x2 = '{:.2f} - {:.2f}i'.format(b2a, d2a)
        
        print(f'As raízes são: {x1} e {x2}')
        return x1, x2
    
    x1 = (-b + m.sqrt(delta)) / (2 * a)
    x2 = (-b - m.sqrt(delta)) / (2 * a)
    
    print(f'As raízes são: {x1} e {x2}')
    return x1, x2
        

           
second_degree_formula(a, b, c)