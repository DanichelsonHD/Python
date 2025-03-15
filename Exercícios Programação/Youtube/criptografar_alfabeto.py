word: str = input('Digite a palavra: ')

def encryption (w: str) -> list[str]:
    alphabet: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters_word: list[str] = [i for i in w]
    numbers: list[str] = [(1 + alphabet.index(i)) for i in letters_word]
    return numbers

print(encryption(word))