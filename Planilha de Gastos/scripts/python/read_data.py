import pandas as pd
from js import console, window

file_path = './src/database.xlsx'
data = pd.read_excel(file_path)
df = pd.DataFrame(data)

type = df['Categoria']
date = df['Data']
place = df['Local']
price = df['Preço']
unity = df['Unidade']
quantity = df['Quantia']
name = df['Produto']

def sum_by_type (t: str) -> int:
    sum: int = 0
    
    for i in range(0, len(type)):
        if type[i] == t:
            sum += float(price[i])
    console.log(sum)
    
    return sum

sum_by_type('Comida')