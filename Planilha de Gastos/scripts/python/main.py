import plotly as plt
import pandas as pd
import openpyxl
import read_data as rd
import manage_data as md
from js import console, window

console.log('Rodou o script main.py')

action = window.prompt('O que deseja fazer? \n[1] Deletar tudo \n[2] Deletar última entrada \n[3] Deletar por índice \n[4] Adicionar a base de dados: ')

md.terminal(action)
console.log(rd.sum_by_type('Comida'))