number: int = int(input('Digite um número: '))

def sum_prime_numbers (n: int):
    sum: int = 0
    for i in range(1, n + 1):
        if divisors(i) == 2:
            sum += i
    print(sum)
    return sum

def divisors (i: int):
    divisors: int = 0
    for j in range (1, i + 1):
        if i % j == 0:
            divisors += 1
    return divisors
            
sum_prime_numbers(number)