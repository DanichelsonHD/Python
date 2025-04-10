import pandas as pd
import datetime as dt

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

def delete_all_data (delete: str):
    if delete == 'exterminador':
        empty_df = pd.DataFrame(columns=df.columns)
        empty_df.to_excel(file_path, index=False)
    
        print('All data deleted')

def delete_last_data (delete: str):
    global df
    if delete == 'sim':
        if not df.empty:
            df = df.iloc[:-1]
            df.to_excel(file_path, index=False)
    
            print('Last data deleted')

def delete_by_index (index: int):
    global df
    if index in df.index:
        df = df.drop(index)
        df.reset_index(drop=True, implace=True)
        df.to_excel(file_path, index=False)
        
        print(f'Data on index {index} deleted')
    else:
        print(f"Couldn't find index {index}")
        

def update_excel (addType, addPlace, addDate, addPrice, newUnity, newQuantity, addName):
    newData = update_data_of_excel(addType, addPlace, addDate, addPrice, newUnity, newQuantity, addName)
    df = pd.concat([data, pd.DataFrame(newData)], ignore_index=True)

    df.to_excel(file_path, index=False)

    print('Excel updated')

def get_info_to_add (newType, newPlace, newDate, newPrice, newUnity, newQuantity, newName):
    if verify_info(newType, newDate, newPrice, newUnity, newQuantity):
        update_excel(newType, newPlace, newDate, newPrice, newUnity, newQuantity, newName)
    else:
        print('Invalid info')
        get_info_to_add(newType, newPlace, newDate, newPrice, newUnity, newQuantity, newName)
        
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

def terminal (action: str = input('O que deseja fazer? [1] Deletar tudo, [2] Deletar última entrada, [3] Deletar por índice, [4] Adicionar a base de dados: ')):
    match action:
        case '1':
            delete_all_data(delete = input('Deletar tudo? '))
        
        case '2':
            delete_last_data(delete = input('Deletar última entrada? '))
            
        case '3':
            delete_by_index(index = input('Índice da informação a ser deletada: '))
            
        case '4':
            get_info_to_add(
                newType = input('Categoria: '),
                newPlace = input('Local: '),
                newDate = input('Data: '),
                newPrice = input('Preço: '),
                newUnity = input('Unidade de Medida: '),
                newQuantity = input('Quantidade: '),
                newName = input('Produto: ')
                )
            
        case _:
            print('Invalid Number')

terminal()