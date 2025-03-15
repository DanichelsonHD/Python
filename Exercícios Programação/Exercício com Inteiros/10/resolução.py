def main():
    '''
    Programa que lê um inteiro positivo n e imprime uma mensagem
    indicando se ele é ou não triangular
    '''

    print("Determina se um número n é triangular\n")

    # leia o valor de n
    n = int(input("Digite o valor de n: "))

    
    i = 1
    while i * (i+1) * (i+2) < n:
        i = i + 1
  
    if i * (i+1) * (i+2) == n:
        print("%d é o produto %d*%d*%d" %(n,i,i+1,i+2))
    else:
        print("%d não é triangular" %(n))
  
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()