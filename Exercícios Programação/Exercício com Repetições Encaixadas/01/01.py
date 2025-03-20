number: int = int(input('Digite um número para o total de listas: '))

def calc_sum (number: int):
    sum_list: list[int] = []
    
    for i in range(1, number + 1):
        sum = 0
        number_list: list[int] = []
        add_numbers_to_list(number_list, i)
        
        for j in range(len(number_list)):
            if number_list[j] % 2 == 0:
                sum += number_list[j]
                
        sum_list.append(sum)
    
    for k in range(len(sum_list)):
        print(f'Soma dos números pares da lista {k + 1}: {sum_list[k]}')
        
    return sum_list
        
def add_numbers_to_list (nL: list[int], i: int):
    new_number: int = int(input(f'Adicione um número a lista {i}: '))
    
    if new_number != 0:
        nL.append(new_number)
        add_numbers_to_list(nL, i)

calc_sum(number)