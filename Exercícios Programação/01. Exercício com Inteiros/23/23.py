number: str = input('Digite um número inteiro: ')

def verify_palindrome (n: str) -> bool:
    for i in range(0, len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            print(f'O número {n} não é palíndromo')
            return False
        
    print(f'O número {n} é palíndromo')
    return True
        
verify_palindrome(number)
    