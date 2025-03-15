def convert_number_to_letter (number: int) -> list[str]:
    
    alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_to_print: list[str] = []
    
    while number > 26:
        print('Número inválido')
        return ['']
    if number <= 0: 
        print('Número inválido')
        return ['']
    
    for i in range(number):
        letters_to_print.append(alphabet[i])
    
    print(letters_to_print)
    return letters_to_print

convert_number_to_letter(int(input('Digite um número: ')))