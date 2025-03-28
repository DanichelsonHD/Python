def calc_sum (sum: int, total_pairs: int) -> int:
    a: int = int(input('Digite um número inteiro: '))
    b: int = int(input('Digite outro número inteiro: '))
    
    if a != 0:
        total_pairs += 1
        sum += a**b
        
        print(f'Par: ({a}, {b})')
        print('Resp:', a**b)
        print('Sum:', sum)
        calc_sum(sum, total_pairs)
    else:     
        print(f'Foram lidos {total_pairs} pares de números.')
        return sum

calc_sum(0, 0)