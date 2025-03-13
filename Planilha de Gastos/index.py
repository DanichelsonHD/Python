import pandas as pd

place: list[str]
type: list[str]
date: list[str]
price: list[str]

file_path = 'database.xlsx'
data = pd.read_excel(file_path)
df = pd.DataFrame(data)

def update_data (addType, addPlace, addDate, addPrice):
    type.append(addType)
    place.append(addPlace)
    date.append(addDate)
    price.append('R$ ' + addPrice)
    
    newData = {
        'Data': date,
        'Local': place,
        'Categoria': type,
        'Preço': price
    }

    return newData

def delete_data (delete = input('Deletar tudo? ')):
    if (delete == 'exterminador'):
        empty_df = pd.DataFrame(columns=df.columns)
        empty_df.to_excel(file_path, index=False)
    
        print('Data deleted')

def update_excel (addType, addPlace, addDate, addPrice):
    newData = update_data(addType, addPlace, addDate, addPrice)
    df = pd.concat([data, pd.DataFrame(newData)], ignore_index=True)

    df.to_excel(file_path, index=False)

    print('Excel updated')


#delete_data()
newType = input('Categoria: ')
newPlace = input('Lugar: ')
newDate = input('Data: ')
newPrice = input('Preço: ')

update_excel(newType, newPlace, newDate, newPrice)

