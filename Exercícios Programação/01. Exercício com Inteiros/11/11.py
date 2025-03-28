number: int = int(input("Digite um número: "))

def verify_if_prime (n: int):
    if n == 1: print("Não é primo.")
    else:
        counter: int = 0
        for i in range(1, n + 1):
            if n % i == 0: counter += 1
            
        if counter == 2: print("É primo.")
        else: print("Não é primo.")

verify_if_prime(number)