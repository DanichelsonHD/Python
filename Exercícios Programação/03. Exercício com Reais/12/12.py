def sum1 ():
    signal: int = 1
    sum: float = 0
    
    for i in range(1, 10001):
        sum += signal * 1 / i
        signal *= -1
    
    print(sum)

def sum2 ():
    signal: int = -1
    sum: float = 0
    i: int = 10000
    
    while i > 0:
        sum += signal * 1 / i
        signal *= -1
        i -= 1
    
    print(sum)
    
def sum3 ():
    sum: float = 0
    neg: float = 0
    pos: float = 0
    
    for i in range(1, 10001):
        if i % 2 != 0:
            pos += 1 / i
        else:
            neg -= 1 / i
    
    sum = neg + pos
    print(f'{pos} + {neg} = {sum}')

def sum4 ():
    sum: float = 0
    neg: float = 0
    pos: float = 0
    i: int = 10000
    
    while i > 0:
        if i % 2 != 0:
            pos += 1 / i
        else:
            neg -= 1 / i
        i -= 1
    
    sum = neg + pos
    print(f'{pos} + {neg} = {sum}')

sum1()
sum2()
sum3()
sum4()