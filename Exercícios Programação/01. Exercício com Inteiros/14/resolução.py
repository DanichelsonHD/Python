def main():
    '''
    Programa que lê um inteiro positivos n e imprime o n-ésimo
    número de Fibonacci F_n.

    F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5  = 5, ...
    '''

    print("Calcula o n-=esimo número de Fibonacci\n")

    # leia o valor de n
    n = int(input("Digite o valor de n (n > 0): "))

    f_ant   = 0
    f_atual = 1
    i       = 1  
  
    while i < n: # antes da comparação vale que f_atual == F(i)
        f_prox  = f_ant + f_atual
        f_ant   = f_atual
        f_atual = f_prox
        i       = i + 1

    print("F(%d) = %d" %(n,f_atual))
  
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()
