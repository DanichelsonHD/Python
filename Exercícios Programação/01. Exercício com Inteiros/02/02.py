def calc_sum (number: int):
    sum: int = 0
    i: int = 1
    for i in range(1, number + 1):
        sum += i
    print(sum)
    
calc_sum(int(input("Digite um número inteiro: ")))