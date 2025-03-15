n: int = int(input('Digite um número inteiro: '))

def verify_if_is_triangular (number: int):
    i: int = 1
    while number > i * (i + 1) * (i + 2):
        i += 1
    if number == (i * (i + 1) * (i + 2)):
        print("Esse número é triangular")
        print("{} x {} x {}".format(i, i + 1, i + 2))
    else:
        print("Esse número não é triangular")
        
verify_if_is_triangular(n)