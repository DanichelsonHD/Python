numbers_1: str = input('Digite um número com vários dígitos: ')
numbers_2: str = input('Digite outro número com a mesma quantia de dígitos: ')

def verify_digits (n1: str, n2: str) -> bool:
    number_list: list[int] = []
    count_numbers: list[str] = []
    counter: int = 1
    
    if len(n1) != len(n2):
        print('Quantia de algarismos diferente dentre si')
        return False
    
    for number in n1:
        number_list.append(int(number))
        
    number_list.sort()
    number_list.append(0)
    
    for i in range(0, len(number_list) - 1):
        if number_list[i] == number_list[i + 1]:
            counter += 1
        else:
            count_numbers.append(f'{number_list[i]}x{counter}')
            counter = 1
    
    for number in n2:
        number = int(number)
        
        if number in number_list:
            number_list.remove(number)
        else:
            print('Algarismos desiguais')
            return False
    
    print('Os dois compartilham os mesmos algarismos')
    print(count_numbers)
    return True    

verify_digits(numbers_1, numbers_2)