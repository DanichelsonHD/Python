import math as m

x: int = int(input("Digite um número: "))
n: int = int(input("Digite outro número: "))

def print_exponentiation (x: int, n: int):
    print("O número {} elevado ao número {}, é: ".format(x, n) + calc_exponentiation(x, n))
    
def calc_exponentiation (x: int, n: int):
    return str(int(m.pow(x, n)))

print_exponentiation(x, n)