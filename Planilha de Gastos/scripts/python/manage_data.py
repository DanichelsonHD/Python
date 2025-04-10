import pandas as pd
import datetime as dt
from js import console, window

file_path = './src/database.xlsx'
data = pd.read_excel(file_path)
df = pd.DataFrame(data)

def update_data_of_excel (addType, addPlace, addDate, addPrice, addUnity, addQuantity, addName):
    newData = {
        'Data': [addDate],
        'Produto': [addName],
        'Local': [addPlace],
        'Categoria': [addType],
        'Preço': [addPrice],
        'Unidade': [addUnity],
        'Quantia': [addQuantity]
    }

    return newData

def delete_all_data (delete: str) -> str:
    if delete == 'exterminador':
        empty_df = pd.DataFrame(columns=df.columns)
        empty_df.to_excel(file_path, index=False)
    
        return 'All data deleted'

def delete_last_data (delete: str) -> str:
    global df
    if delete == 'sim':
        if not df.empty:
            df = df.iloc[:-1]
            df.to_excel(file_path, index=False)
    
            return 'Last data deleted'

def delete_by_index (index: int) -> str:
    global df
    if index in df.index:
        df = df.drop(index)
        df.reset_index(drop=True, implace=True)
        df.to_excel(file_path, index=False)
        
        return f'Data on index {index} deleted'
    else:
        return f"Couldn't find index {index}"
        

def update_excel (addType, addPlace, addDate, addPrice, newUnity, newQuantity, addName) -> str:
    newData = update_data_of_excel(addType, addPlace, addDate, addPrice, newUnity, newQuantity, addName)
    df = pd.concat([data, pd.DataFrame(newData)], ignore_index=True)

    df.to_excel(file_path, index=False)

    return 'Excel updated'

def get_info_to_add (newType, newPlace, newDate, newPrice, newUnity, newQuantity, newName):
    if verify_info(newType, newDate, newPrice, newUnity, newQuantity):
        update_excel(newType, newPlace, newDate, newPrice, newUnity, newQuantity, newName)
    else:
        get_info_to_add(newType, newPlace, newDate, newPrice, newUnity, newQuantity, newName)
        return 'Invalid info'
        
def verify_info(newType, newDate, newPrice, newUnity, newQuantity) -> bool:
    valid_types: list[str] = ['Comida', 'Higiene', 'Limpeza', 'Vestuario', 'Eletronico', 'Pets', 'Saude', 'Passeio', 'Carro', 'Dizimo']
    
    valid_unitys: list[str] = ['Kg', 'L', 'U']
    
    if not (newType in valid_types):
        return False
    
    if not (dt.datetime.strptime(newDate, '%d/%m/%Y')):
        return False
    
    if not (newUnity in valid_unitys):
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
            delete_all_data('exterminador')
        
        case '2':
            delete_last_data('sim')
            
        case '3':
            delete_by_index(window.prompt('Índice da informação a ser deletada: '))
            
        case '4':
            get_info_to_add(
                newType = window.prompt('Categoria: '),
                newPlace = window.prompt('Local: '),
                newDate = window.prompt('Data: '),
                newPrice = window.prompt('Preço: '),
                newUnity = window.prompt('Unidade de Medida: '),
                newQuantity = window.prompt('Quantidade: '),
                newName = window.prompt('Produto: ')
                )
            
        case _:
            return 'Invalid Number'

terminal()