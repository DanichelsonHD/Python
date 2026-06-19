from unidecode import unidecode

# Caminhos
arquivo_palavras_sem_acentos = "palavras_sem_acentos.txt"
arquivo_palavras_com_acentos = "palavras_com_acentos.txt"
arquivo_frequentes = "5milPalavrasComuns.txt"

# Carrega lista de palavras frequentes
palavras_frequentes = set()

with open(arquivo_frequentes, "r", encoding="utf-8") as f:
    for linha in f:
        palavra = linha.split()[0].strip().lower()
        if len(palavra) == 5 and palavra.isalpha():
            palavras_frequentes.add(unidecode(palavra))

# Lê todas as palavras com acento
with open(arquivo_palavras_com_acentos, "r", encoding="utf-8") as f:
    palavras_com_acentos = [linha.strip() for linha in f if len(linha.strip()) == 5]

# Filtra com base na versão sem acento
palavras_filtradas = []
for palavra in palavras_com_acentos:
    sem_acento = unidecode(palavra)
    if sem_acento in palavras_frequentes:
        palavras_filtradas.append(palavra)

# Gera novas listas reduzidas
with open("palavras_reduzidas_com_acentos.txt", "w", encoding="utf-8") as f:
    for p in sorted(palavras_filtradas):
        f.write(p + "\n")

with open("palavras_reduzidas_sem_acentos.txt", "w", encoding="utf-8") as f:
    for p in sorted(unidecode(p) for p in palavras_filtradas):
        f.write(p + "\n")

print(f"{len(palavras_filtradas)} palavras mantidas com base na lista comum.")