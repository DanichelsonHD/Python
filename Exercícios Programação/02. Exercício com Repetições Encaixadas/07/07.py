def calc_all_mdc ():
    number: int = int(input('Digite um número para limitar a lista: '))
    number_list: list[int] = [int(input('Digite números para colocar na lista: ')) for _ in range(number)]
    
    mdc: int = number_list[0]
    
    for n in range(1, len(number_list)):
        mdc = get_mdc(number_list[n], mdc)
    
    print(f'O MDC dos números {', '.join(str(j) for j in number_list)} é: {mdc}')
    
def get_mdc (current: int, mdc: int):
    while mdc != 0:
        current, mdc = mdc, current % mdc
    return current

calc_all_mdc()