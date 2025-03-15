#-----------------------------------------------------------------
# Solução 1: usa while e formato %d para imprimir a resposta
#
#----------------------------------------------------------------
def main():
    '''
    Programa que lê um número inteiro n >= 0 e imprime n!
    '''

    print("Cálculo do fatorial de um número\n")

    # leia o valor de n
    n = int(input("Digite um número inteiro não-negativo: "))

    # inicializações
    i     = 1  # contador
    n_fat = 1  

    # calcule n!
    while i <= n:
        n_fat = n_fat * i 
        i = i + 1

    print("%d! = %d" %(n, n_fat))     
        
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()

#-----------------------------------------------------------------
# Solução 2: usa o comando for ... in range(...)
#
#-----------------------------------------------------------------
def main():
    '''
    Programa que lê um número inteiro n >= 0 e imprime n!
    '''

    print("Cálculo do fatorial de um número\n")

    # leia o valor de n
    n = int(input("Digite um número inteiro não-negativo: "))

    # inicialização da variável que armazena os fatoriais
    n_fat = 1

    # calcule n!
    for i in range(2,n+1):
        n_fat = n_fat * i 

    print("%d! = %d" %(n, n_fat))     
        
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()