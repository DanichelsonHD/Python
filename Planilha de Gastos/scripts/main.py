import pandas as pd
from js import console, window, document
import datetime as dt
from pyodide.http import open_url

file_path = './src/database.csv'
response = open_url(file_path)
data = pd.read_csv(response, delimiter=";", decimal=",", on_bad_lines='skip')
df = pd.DataFrame(data)

console.log('Rodou o script main.py')

#action = window.prompt('O que deseja fazer? \n[1] Deletar tudo \n[2] Deletar última entrada \n[3] Deletar por índice \n[4] Adicionar a base de dados: ')
#md.terminal(action)

class manage_data:
    valid_types: list[str] = ['Comida', 'Higiene', 'Limpeza', 'Vestuario', 'Eletronico', 'Pets', 'Saude', 'Passeio', 'Carro', 'Dizimo']
    valid_unities: list[str] = ['Kg', 'L', 'U']

    def update_data_of_excel (addType, addPlace, addDate, addPrice, addUnity, addQuantity, addName):
        newData = {
            'Data': [addDate],
            'Produto': [addName],
            'Local': [addPlace],
            'Categoria': [addType],
            'Preco': [addPrice],
            'Unidade': [addUnity],
            'Quantia': [addQuantity]
        }

        return newData

    def delete_all_data (delete: str) -> str:
        if delete == 'exterminador':
            empty_df = pd.DataFrame(columns=df.columns)
            empty_df.to_csv(file_path, index=False, delimiter=";", decimal=",")
        
            console.log('All data deleted')

    def delete_last_data (delete: str) -> str:
        global df
        if delete == 'sim':
            if not df.empty:
                df = df.iloc[:-1]
                df.to_csv(file_path, index=False, delimiter=";", decimal=",")
        
                console.log('Last data deleted')

    def delete_by_index (index: int) -> str:
        global df
        if index in df.index:
            df = df.drop(index)
            df.reset_index(drop=True, implace=True)
            df.to_csv(file_path, index=False, delimiter=";", decimal=",")
            
            return f'Data on index {index} deleted'
        else:
            return f"Couldn't find index {index}"
            

    def update_excel (addType, addPlace, addDate, addPrice, newUnity, newQuantity, addName) -> str:
        newData = manage_data.update_data_of_excel(addType, addPlace, addDate, addPrice, newUnity, newQuantity, addName)
        df = pd.concat([data, pd.DataFrame(newData)], ignore_index=True)

        df.to_csv(file_path, index=False, delimiter=";", decimal=",")

        console.log('Excel updated')

    def get_info_to_add (newType, newPlace, newDate, newPrice, newUnity, newQuantity, newName):
        if manage_data.verify_info(newType, newDate, newPrice, newUnity, newQuantity):
            manage_data.update_excel(newType, newPlace, newDate, newPrice, newUnity, newQuantity, newName)
        else:
            manage_data.get_info_to_add(newType, newPlace, newDate, newPrice, newUnity, newQuantity, newName)
            console.log('Invalid info')
            
    def verify_info(newType, newDate, newPrice, newUnity, newQuantity) -> bool:     
        if not (newType in manage_data.valid_types):
            return False
        
        if not (dt.datetime.strptime(newDate, '%d/%m/%Y')):
            return False
        
        if not (newUnity in manage_data.valid_unities):
            return False
        
        try:
            newPrice = float(newPrice)
            newPrice = f"{float(newPrice):.2f}"
            newQuantity = int(newQuantity)
        except ValueError:
            return False
        
        return True

    def terminal (action: str):
        match action:
            case '1':
                manage_data.delete_all_data(window.prompt('Confirme: '))
            
            case '2':
                manage_data.delete_last_data(window.prompt('Confirme: '))
                
            case '3':
                manage_data.delete_by_index(window.prompt('Índice da informação a ser deletada: '))
                
            case '4':
                manage_data.get_info_to_add(
                    newType = window.prompt(f'Categorias aceitas {manage_data.valid_types}: '),
                    newPlace = window.prompt('Local: '),
                    newDate = window.prompt('Data [00/00/0000]: '),
                    newPrice = window.prompt('Preço [00,00]: '),
                    newUnity = window.prompt(f'Unidades de Medida aceitas {manage_data.valid_unities}: '),
                    newQuantity = window.prompt('Quantidade: '),
                    newName = window.prompt('Produto: ')
                    )
                
            case _:
                console.log('Invalid Number')

class read_data:
    global df
    type = df['Categoria']
    date = df['Data']
    place = df['Local']
    price = df['Preco']
    unity = df['Unidade']
    quantity = df['Quantia']
    name = df['Produto']
    
    categories: list[str] = df.columns.tolist()

    def return_categories (): 
        return read_data.categories
    
    def sum_by_type (t: str) -> int:
        sum: int = 0
        
        for i in range(0, len(type)):
            if type[i] == t:
                sum += float(read_data.price[i])
        
        return sum

class display_data:
    global df

    table = document.getElementsByClassName('table')[0]

    def display_data_on_table ():
        index: int = 0
        for row in df.iterrows():
            display_data.add_childs_to_table(display_data.table, index)
            index += 1
    
    def add_childs_to_table (table, index):
        categories = read_data.return_categories()
        row_html = '<tr class="tabela">'
        
        for category in categories:
            display = df[category][index]
            
            if category == 'Preco':
                display = f'R$ {float(display):.2f}'
            
            row_html += f'<td>{display}</td>'
        
        row_html += '</tr>'
        table.innerHTML += row_html 

display_data.display_data_on_table()