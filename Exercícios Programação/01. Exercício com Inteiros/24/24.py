number_q: int = int(input('Digite um número com vários digitos: '))
number_p: int = int(input('Outro número com menos/mesma quantia de digitos: '))

def verify_p_in_q (p: int, q: int) -> bool:
    p = str(p)
    q = str(q)
    
    if p in q:
        print(f'{p} está contido em {q}')
        return True
    else:
        print(f'{p} não está contido em {q}')
        return False

verify_p_in_q(number_p, number_q)