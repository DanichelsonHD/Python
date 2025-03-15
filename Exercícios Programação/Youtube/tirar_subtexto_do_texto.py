text: str = input('Digite uma frase: ')
subtext: str = input('Digite uma palavra da frase: ')

def subtract_subtext_from_text (t: str, st: str) -> str:
    text_list: list[str] = t.split(' ')
    new_text_list: list[str] = [i for i in text_list if i != st]
    new_text: str = ' '.join(new_text_list)
    return new_text

print(subtract_subtext_from_text(text, subtext))