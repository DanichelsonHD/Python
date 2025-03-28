number: int = int(input("Digite um número: "))

def calc_hypotenuse (n: int):
    hypotenuses: list[int] = []
    
    for i in range(1, n + 1):
        for c1 in range(1, i):         
            for c2 in range(c1, i):
                if i not in hypotenuses:
                    if c1 ** 2 + c2 ** 2 == i ** 2:
                        hypotenuses.append(i)     
                        continue
    
    print(f"Os números que são hipotenusas são: {hypotenuses}")
    return hypotenuses

calc_hypotenuse(number)