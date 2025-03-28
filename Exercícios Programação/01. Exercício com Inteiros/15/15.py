n: int = int(input('Digite um número inteiro: '))
j: int = int(input('Digite outro número inteiro: '))
m: int = int(input('Digite mais um número inteiro: '))

def calc_congruent_mod_numbers (n: int, j: int, m: int):
    counter: int = 0
    i: int = 0
    number_list: list = []
    while counter < n:
        if i % m == j % m:
            number_list.append(i)
            counter += 1
        i += 1
    
    print(number_list)

calc_congruent_mod_numbers(n, j, m)