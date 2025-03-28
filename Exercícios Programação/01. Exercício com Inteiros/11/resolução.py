#------------------------------------------------------------------
# Solução 1: Usa uma variável indicadora de passagem (booleana) 
#            é_primo
#
#------------------------------------------------------------------
def main():
    '''
    Programa que lê um inteiro positivo n e imprime uma mensagem
    indicando se ele é ou não triangular.

    Observacao: um número inteiro é primo se ele é maior do que 1
        e seus únicos divisores são ele mesmo e 1. 
        Assim, 1 não é primo.

    Exemplos de execução

    Digite o valor de n (n > 0): 1
    1 não é primo

    Digite o valor de n (n > 0): 4
    4 não é primo

    Digite o valor de n (n > 0): 27644437
    27644437 é primo
    '''

    print("Determina se um número n > 0 é primo\n")

    # leia o valor de n
    n = int(input("Digite o valor de n (n > 0): "))

    # n é primo até que se prove o contrário
    é_primo = True

    # procure por um divisor de n entre 2 e n-1
    divisor = 2
    while divisor < n and é_primo: # equivalente a "div... and é_primo == True:"
        if n % divisor == 0:
            é_primo = False
        divisor += 1
  
    
    if é_primo and n != 1: # 1 não é primo
        print(n, "é primo")
    else:
        print(n, "não é primo")

  
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()

#------------------------------------------------------------------
# Solução 2: Conta os divisores de n entre 1 e n
#            
#------------------------------------------------------------------
def main():
    '''
    Programa que lê um inteiro positivo n e imprime uma mensagem
    indicando se ele é ou não triangular.

    Observacao: um número inteiro é primo se ele é maior do que 1
        e seus únicos divisores são ele mesmo e 1. 
        Assim, 1 não é primo.

    Exemplos de execução

    Digite o valor de n (n > 0): 1
    1 não é primo

    Digite o valor de n (n > 0): 4
    4 não é primo

    Digite o valor de n (n > 0): 27644437
    27644437 é primo
    '''

    print("Determina se um número n > 0 é primo\n")

    # leia o valor de n
    n = int(input("Digite o valor de n (n > 0): "))

    # inicialize o contador de número divisores de n
    cont_divisores = 0

    # conta o número de divisores entre 1 e n
    for divisor in range(1,n+1):
        if n % divisor == 0:
            cont_divisores += 1 

    # imprima mensagem
    if cont_divisores == 2:
        print(n, "é primo")
    else:
        print(n, "não é primo")

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()

#------------------------------------------------------------------
# Solução 3: Essencialmente idêntica à solução 1,  um pouco mais
#            eficiente já que dentro do while só testa divibilidade
#            por números ímpares.
#
#------------------------------------------------------------------
def main():
    '''
    Programa que lê um inteiro positivo n e imprime uma mensagem
    indicando se ele é ou não triangular.

    Observacao: um número inteiro é primo se ele é maior do que 1
        e seus únicos divisores são ele mesmo e 1. 
        Assim, 1 não é primo.

    Exemplos de execução

    Digite o valor de n (n > 0): 1
    1 não é primo

    Digite o valor de n (n > 0): 4
    4 não é primo

    Digite o valor de n (n > 0): 27644437
    27644437 é primo
    '''

    print("Determina se um número n > 0 é primo\n")

    # leia o valor de n
    n = int(input("Digite o valor de n (n > 0): "))

    # n é primo até que se prove o contrário
    if n == 2 or (n != 1 and n % 2 == 1): # 2 é primo , 1 não é primo
        é_primo = True
    else:
        é_primo = False  # pares maiores que 2 não são primos

    # procure por um divisor ímpar de n entre 2 e n-1
    divisor = 3
    while divisor < n and é_primo: # equivalente a "div ... and é_primo == True:"
        if n % divisor == 0:
            é_primo = False
        divisor += 2 
  
    
    if é_primo: 
        print(n, "é primo");
    else:
        print(n, "não é primo");

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()

#------------------------------------------------------------------
# Solução 4: Essencialmente idêntica à solução 3,   um pouco mais
#            eficiente já que dentro do while só testa divibilidade
#            por números ímpares menores que n//2.
#     
#            Poderíamos ainda usar o fato de que se um número
#            n possui um divisor maior que 1, então ele possui
#            um divisor maior que 1 e menor ou igual a raiz quadrada
#            de n.
#
#------------------------------------------------------------------
def main():
    '''
    Programa que lê um inteiro positivo n e imprime uma mensagem
    indicando se ele é ou não triangular.

    Observacao: um número inteiro é primo se ele é maior do que 1
        e seus únicos divisores são ele mesmo e 1. 
        Assim, 1 não é primo.

    Exemplos de execução

    Digite o valor de n (n > 0): 1
    1 não é primo

    Digite o valor de n (n > 0): 4
    4 não é primo

    Digite o valor de n (n > 0): 27644437
    27644437 é primo
    '''

    print("Determina se um número n > 0 é primo\n")

    # leia o valor de n
    n = int(input("Digite o valor de n (n > 0): "))

    # n é primo até que se prove o contrário
    if n == 2 or (n != 1 and n % 2 == 1): # 2 é primo , 1 não é primo
        é_primo = True
    else:
        é_primo = False  # pares maiores que 2 não são primos

    # procure por um divisor ímpar de n entre 2 e n-1
    divisor = 3
    while divisor < n // 2 and é_primo: # equivalente a "div ... and é_primo == True:"
        if n % divisor == 0:
            é_primo = False
        divisor += 2 
  
    
    if é_primo: 
        print(n, "é primo");
    else:
        print(n, "não é primo");

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()