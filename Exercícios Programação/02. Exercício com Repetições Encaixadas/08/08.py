number_n: int = int(input('Digite um número para o tamanho da lista: '))
number_list: list[int] = [int(input('Digite números para colocar na lista: ')) for _ in range(number_n)]
number_k: int = int(input('Digite um número para separar em grupos: '))

def verify_if_k_alternating (n: int, n_list: list[int], k: int):
    if n % k != 0:
        print('Não é possível dividir')
        return False
    
    previous_parity: str = None
    
    for i in range(0, n, k):
        segment: list[int] = n_list[i:i + k]
        
        current_parity = 'even' if segment[0] % 2 == 0 else 'odd'
        for num in segment:
            if (num % 2 == 0 and current_parity != 'even') or (num % 2 != 0 and current_parity != 'odd'):
                print('A sequência não é k-alternante')
                return False
            
        if previous_parity and previous_parity == current_parity:
            print('A sequência não é k-alternante')
            return False
        
        previous_parity = current_parity
    
    print(f'A sequência é {k}-alternante')
    return True

        

verify_if_k_alternating(number_n, number_list, number_k)