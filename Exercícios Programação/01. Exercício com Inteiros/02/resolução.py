#------------------------------------------------------------------
# Solução 1
#------------------------------------------------------------------
def main():
    '''
    Programa que lê um inteiro positivo n e imprime o valor da soma
    1 + 2 + 3 + ... + n.

    Exemplos de execução:

    >>> 
    Cálculo da soma dos n primeiros inteiros positivos
    Digite o valor de n: 3
    A soma dos 3 primeiros inteiros positivos é 6
    >>> 
    Calculo da soma dos n primeiros inteiros positivos
    Digite o valor de n: 10
    A soma dos 10 primeiros inteiros positivos é 55
    >>> 
    Calculo da soma dos n primeiros inteiros positivos
    Digite o valor de n: 0
    A soma dos 0 primeiros inteiros positivos é 0
    >>> 
    '''

    print("Calculo da soma dos n primeiros inteiros positivos")

    # leia o valor de n
    n = int(input("Digite o valor de n: "))

    # inicialize a soma
    soma = 0

    # calcule a soma
    i = 1
    while i <= n:
        soma = soma + i
        i = i + 1

    # imprima a soma
    print("A soma dos", n, "primeiros inteiros positivos é", soma)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()


#------------------------------------------------------------------
# Solução 2
#------------------------------------------------------------------
def main():
    '''
    Programa que lê um inteiro positivo n e imprime o valor da soma
    1 + 2 + 3 + ... + n.

    Exemplos de execução:

    >>> 
    Cálculo da soma dos n primeiros inteiros positivos
    Digite o valor de n: 3
    A soma dos 3 primeiros inteiros positivos é 6
    >>> 
    Calculo da soma dos n primeiros inteiros positivos
    Digite o valor de n: 10
    A soma dos 10 primeiros inteiros positivos é 55
    >>> 
    Calculo da soma dos n primeiros inteiros positivos
    Digite o valor de n: 0
    A soma dos 0 primeiros inteiros positivos é 0
    >>> 
    
    '''

    print("Calculo da soma dos n primeiros inteiros positivos")

    # leia o valor de n
    n = int(input("Digite o valor de n: "))

    # calcule a soma de uma PA de razão 1
    soma = n * (n + 1) // 2 # divisão inteira

    # imprima a soma
    print("A soma dos", n, "primeiros inteiros positivos é", soma)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()