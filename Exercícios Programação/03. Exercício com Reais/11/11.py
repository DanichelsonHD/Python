number: int = int(input('Digite um número: '))

def sum (n: int):
    sum: int = 0
    for i in range(1, n + 1):
        sum += i / (n - i + 1)
        print(f'{i} / {n - i + 1} = {i / (n - i + 1)}')
        
    print(sum)

sum(number)