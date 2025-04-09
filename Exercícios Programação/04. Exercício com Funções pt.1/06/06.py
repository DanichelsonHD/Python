def euclides_mdc (a:int, b:int):
    while b != 0:
        a, b = b, a % b
        
    return a

number_n: int = int(input("Digite o primeiro número: "))

def mdc_all_numbers(n: int):
    numbers: list[int] = [int(input(f"Digite o {_+1}º número: ")) for _ in range(n)]
    
    mdc: int = numbers[0]
    
    for i in range(1, n):
        mdc = euclides_mdc(mdc, numbers[i])
    
    return mdc

print(mdc_all_numbers(number_n))
        