import plotly as plt
import pandas as pd
import openpyxl
import read_data as rd
import manage_data as md
from js import console, window, document

console.log('Rodou o script main.py')

#action = window.prompt('O que deseja fazer? \n[1] Deletar tudo \n[2] Deletar última entrada \n[3] Deletar por índice \n[4] Adicionar a base de dados: ')
#md.terminal(action)

categories: list[str] = rd.return_categories()

table = document.getElementsByClassName('table')[0]

def display_data_on_table ():
    total_tables = len(rd.df)
    print(total_tables)
    
    index: int = 0
    for row in rd.df.iterrows():
        add_childs_to_table(table, index)
        index += 1

def add_childs_to_table (table, index):
    global categories
    row_html = '<tr class="tabela">'
    
    for category in categories:
        display = rd.df[category][index]
        row_html += f'<td>{display}</td>'
    
    row_html += '</tr>'
    table.innerHTML += row_html    
    console.log(table)

display_data_on_table()