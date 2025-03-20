number: int = int(input('Digite um número inteiro: '))

def decimal_to_binary (n: int):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    print(binary)
    
decimal_to_binary(number)