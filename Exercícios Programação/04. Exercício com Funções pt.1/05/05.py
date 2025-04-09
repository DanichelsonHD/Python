def verify_if_prime (m: int) -> int:
    divisors: int = 0
    for i in range(1, m + 1):
        if m % i == 0:
            divisors += 1
    
    if divisors == 2:
        return 1
    
    return 0

def sum_primes (n: int) -> int:
    if n < 0:
        print('Inválido')
        return 0
    
    sum: int = 0
    count: int = 0
    i: int = 2
    
    while count < n:
        if verify_if_prime(i) == 1:
            sum += i
            count += 1
        
        i += 1
    
    print(f'Soma dos {n} primeiros primos é: {sum}')
    return sum

sum_primes(int(input('Digite um número: ')))