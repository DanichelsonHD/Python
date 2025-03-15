#-----------------------------------------------------------------
# Solução 1: curta e grossa
#
#-----------------------------------------------------------------
def main():
    '''
    Programa que lê três números inteiros positivos n, i e j 
    e imprime os n primeiros números inteiros maiores o iguais
    a zero que são multiplos de i ou de j.
    '''

    print("Cálculo dos n primeros multiplos de i ou j\n")

    # leitura dos dados
    n = int(input("Digite n: "))
    i = int(input("Digite i: "))
    j = int(input("Digite j: "))
    
    
    # mult é o candidato a multiplo de i ou j
    mult = 0

    # k é o contador de múltiplos impressos
    k    = 0
    while k < n:
        if mult%i == 0 or mult%j == 0:
            # mult é multiplo de i ou j
            print(mult)
            k = k + 1;
         
        # vamos para o próximo candidato   
        mult = mult + 1;	

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()

#-----------------------------------------------------------------
# Solução 2: Mais elaborada. Faz menos interações que a solução 1.
#            A cada iteração imprime um multiplo de i ou j.
#            Usa o comando for ... in range(...)
#            Usa o comando if ... elif ... else ...
#
#-----------------------------------------------------------------
def main():
    '''
    Programa que lê três números inteiros positivos n, i e j 
    e imprime os n primeiros números inteiros maiores o iguais
    a zero que são múltiplos de i ou de j.
    '''

    print("Cálculo dos n primeros múltiplos de i ou de j\n")

    # leitura dos dados
    n = int(input("Digite n: "))
    i = int(input("Digite i: "))
    j = int(input("Digite j: "))

    # mult_i armazena um múltiplo de i 
    # mult_j armazena um 
    mult_i = mult_j = 0 

    # imprima k múltiplos de i ou de j
    for k in range(n):
        # selecione o menor múltiplo, imprima e passe para o próximo 
        if mult_i == mult_j: 
            print(mult_i)
            mult_i = mult_i + i  # próximo múltiplo de i
            mult_j = mult_j + j  # próximo múltiplo de j
        elif mult_i < mult_j:
            print(mult_i)
            mult_i = mult_i + i  # próximo múltiplo de i
        else: 
            print(mult_j)
            mult_j = mult_j + j; # próximo múltiplo de j

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()
