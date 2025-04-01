def calculator ():
    n1, signal, n2 = map(str, input('Digite uma expressão com 1 sinal (+, -, *, /) e dois números,\nseparando tudo por espaço: ').split(' '))
    n1 = float(n1)
    n2 = float(n2)
    
    match signal:
        case '+':
            print(n1 + n2)
            return n1 + n2
        
        case '-':
            print(n1 - n2)
            return n1 - n2
        
        case '*':
            print(n1 * n2)
            return n1 * n2
        
        case '/':
            print(n1 / n2)
            return n1 / n2
        
        case _:
            print('Error')
            return 'Error'

calculator()