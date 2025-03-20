quantity: int = int(input('Escolha um número pra quantia de elementos: '))
print(f'Digite {quantity} números inteiros:')
sequence: list[int] = [int(input()) for i in range(quantity)]

def count_crescent_segment (q: int, s: list[int]) -> int:
    counter: int = 1
    list_sequences: list[int] = []
    
    for i in range(1, q):
        if s[i] >= s[i - 1]:
            counter += 1
        else:
            list_sequences.append(counter)
            counter = 1
    list_sequences.append(counter)
    
    list_sequences.sort()
    last: int = len(list_sequences) - 1
    print('A maior sequência crescente é: {}'.format(list_sequences[last]))
    return list_sequences[last]
    
count_crescent_segment(quantity, sequence)