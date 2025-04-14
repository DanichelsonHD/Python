import pandas as pd
from js import console
from pyodide.http import open_url

file_path = './src/database.csv'
response = open_url(file_path)
data = pd.read_csv(response, delimiter=";", decimal=",", on_bad_lines='skip')
df = pd.DataFrame(data)

type = df['Categoria']
date = df['Data']
place = df['Local']
price = df['Preco']
unity = df['Unidade']
quantity = df['Quantia']
name = df['Produto']

categories: list[str] = df.columns.tolist()

def return_categories (): 
    console.log(categories)
    return categories

def sum_by_type (t: str) -> int:
    sum: int = 0
    
    for i in range(0, len(type)):
        if type[i] == t:
            sum += float(price[i])
    console.log(sum)
    
    return sum