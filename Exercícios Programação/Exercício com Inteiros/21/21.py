quantity: int = int(input('Escolha um número pra quantia de elementos: '))

def count_segments (q: int):
    print(f'Digite {q} números inteiros:')
    sequence: list[int] = [int(input()) for i in range(q)]
    segments: int = 1
    
    for count in range(1, q):
        if sequence[count] != sequence[count - 1]:
            segments += 1
            
    print("A lista tem", segments, "segmentos")

count_segments(quantity)