def main():
    '''
    Programa que lê um número inteiro x e um número inteiro n maior ou igual 
    a zero e imprime x elevado a n.

    Exemplos de execução:
    
    Digite a base (número inteiro): 3
    Digite o expoente (inteiro >= 0): 3
    O valor de 3 elevado a 3 é 27

    Digite a base (número inteiro): 5
    Digite o expoente (inteiro >= 0): 0
    O valor de 5 elevado a 0 é 1
    '''

    print("Cálculo de potências\n")

    # leia a base
    x = int(input("Digite a base (número inteiro): "))

    # leia o expoente
    n = int(input("Digite o expoente (inteiro >= 0): "))

    # expoente
    i  = 0

    # x elevado a i
    x_i = 1

    # calcule x elevado a n
    while i < n:
        i = i + 1 
        x_i = x_i * x 

    print("O valor de", x, "elevado a", n, "é", x_i)     


# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()


#-------------------------------------------------------------------
# Tentativa de solução ERRADA típica
#-------------------------------------------------------------------

def main():
    '''
    Programa que lê um número inteiro x e um número inteiro n maior ou igual 
    a zero e imprime x elevado a n.

    Este programa está errado.
    '''

    print("Cálculo de potências\n")

    # leia a base
    x = int(input("Digite a base (número inteiro): "))

    # leia o expoente
    n = int(input("Digite o expoente (inteiro >= 0): "))

    # expoente
    i  = 0

    # calcule x elevado a n
    while i < n:
        i = i + 1 
        x = x * x # ERRO: precisamos de uma variável para as potências

    print("O valor de", x, "elevado a", n, "é", x)     


# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()